from flask import Blueprint, request, render_template, send_file, make_response
from datetime import datetime
import pytz
from weasyprint import HTML
import io
import logging

pdf_bp = Blueprint("pdf", __name__)

@pdf_bp.route("/pdf", methods=["GET"])
def generate_pdf_get():
    try:
        borrower = request.args.get("borrower", "Unbekannt").strip()
        device = request.args.get("device", "Unbekannt").strip()
        staff = request.args.get("staff", "IT Support").strip()

        if not borrower or borrower == "Unbekannt":
            if not device or device == "Unbekannt":
                logging.warning("PDF requested with minimal information")

        swiss_tz = pytz.timezone("Europe/Zurich")
        now_swiss = datetime.now(swiss_tz)

        loan_date = now_swiss.strftime("%d.%m.%Y %H:%M")
        return_date = now_swiss.strftime("%d.%m.%Y") + " bis 17:00 Uhr"

        html = render_template(
            "receipt.html",
            borrower=borrower,
            device=device,
            loan_date=loan_date,
            return_date=return_date,
            staff=staff,
        )

        pdf_bytes = HTML(string=html).write_pdf()
        pdf_buffer = io.BytesIO(pdf_bytes)
        pdf_buffer.seek(0)

        safe_borrower = "".join(c for c in borrower if c.isalnum() or c in (" ", "_")).rstrip()
        if not safe_borrower or safe_borrower.isspace():
            safe_borrower = "Unbekannt"

        filename = f"TBZ_Quittung_{safe_borrower.replace(' ', '_')}_{now_swiss.strftime('%Y%m%d_%H%M')}.pdf"

        response = make_response(
            send_file(
                pdf_buffer,
                mimetype="application/pdf",
                as_attachment=True,
                download_name=filename,
            )
        )

        response.headers["Access-Control-Allow-Origin"] = "*"
        response.headers["Access-Control-Allow-Methods"] = "GET"

        logging.info(f"PDF generated successfully for {borrower}, {device}")

        return response

    except Exception as e:
        logging.error(f"PDF generation failed: {str(e)}", exc_info=True)
        return f"Fehler bei PDF Generierung: {str(e)}", 500

@pdf_bp.route("/healthz", methods=["GET"])
@pdf_bp.route("/health", methods=["GET"])
def health_check():
    try:
        render_template(
            "receipt.html",
            borrower="Test",
            device="Test",
            loan_date="01.01.2024 12:00",
            return_date="01.01.2024 bis 17:00 Uhr",
            staff="Test",
        )

        return {
            "status": "healthy",
            "service": "TBZ Geräteausleihe Microservice",
            "endpoints": ["/pdf", "/health", "/healthz"],
            "timestamp": datetime.now(pytz.timezone("Europe/Zurich")).isoformat(),
        }, 200
    except Exception as e:
        logging.error(f"Health check failed: {str(e)}")
        return {"status": "unhealthy", "error": str(e)}, 500

@pdf_bp.route("/pdf", methods=["OPTIONS"])
def pdf_options():
    response = make_response()
    response.headers["Access-Control-Allow-Origin"] = "*"
    response.headers["Access-Control-Allow-Methods"] = "GET, OPTIONS"
    response.headers["Access-Control-Allow-Headers"] = "Content-Type"
    return response

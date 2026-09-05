from reportlab.pdfgen import canvas
from Services.report_collector import calculate_summary
from Services.Data_Fetcher import get_coin_data

coin_data = get_coin_data('bitcoin')
summary = calculate_summary(coin_data)


def generate_pdf(summary):

    c = canvas.Canvas('Report.pdf')

    c.drawString(100, 750, f"{summary['name']} ({summary['symbol']})")
    c.drawString(100, 730, f"Price: ${summary['current_price']}")
    c.drawString(100, 710, f"24h High: ${summary['high_24h']}")
    c.drawString(100, 690, f"24h Low: ${summary['low_24h']}")
    c.drawString(100, 670, f"24h Change: {summary['price_change_percentage_24h']}%")
    c.drawString(100, 650, f"Trend: {summary['trend']}")

    c.save()

generate_pdf(summary)
import unittest

from invoice_ai.amount import extract_amount


class ExtractAmountTests(unittest.TestCase):
    def test_selects_total_instead_of_tax(self):
        self.assertEqual(
            extract_amount("Tiền thuế: 125.000 đ\nTổng thanh toán: 1.375.000 đ"),
            {"status": "ok", "total_amount": 1375000, "source_text": "1.375.000 đ"},
        )

    def test_requests_review_for_invalid_or_ambiguous_input(self):
        for text in (
            "",
            "Tổng thanh toán: 12.50.000 đ",
            "Tổng thanh toán: 1.25O.000 đ",
            "Tổng thanh toán: 100 đ\nTổng thanh toán: 200 đ",
        ):
            with self.subTest(text=text):
                self.assertEqual(extract_amount(text)["status"], "needs_review")

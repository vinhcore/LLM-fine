# Vietnamese Invoice AI

Dự án thực hành AI Engineering theo nguyên lý xe đạp. Đích đến là nhận ảnh hóa đơn tiếng Việt, trích xuất bốn trường có bằng chứng và phục vụ qua API.

## Mục 1 · Từ văn bản OCR đến JSON

Cần Python 3.9 trở lên. Bài này dùng thư viện chuẩn và đầu vào là văn bản OCR mô phỏng.

```bash
python3 -m invoice_ai samples/valid.txt
python3 -m invoice_ai samples/unclear.txt
python3 -m unittest discover -s tests -v
```

Mẫu đầu trả tổng tiền 1375000 và giữ văn bản nguồn. Mẫu thứ hai trả `needs_review` vì OCR đọc chữ S ở vị trí chữ số.

1. **Tháo tung.** Đọc `invoice_ai/__main__.py` để thấy cách Python đọc file và gọi `extract_amount` trong `invoice_ai/amount.py`.
2. **Truy vấn.** Thử đổi tổng thành `12.50.000 đ`. Kiểm tra định dạng phải diễn ra trước khi xóa dấu chấm vì dấu chấm cho biết các nhóm hàng nghìn có đúng ba chữ số hay không.
3. **Lắp lại.** Thêm một mẫu có hai dòng tổng tiền. Viết test để kiểm chứng chương trình chuyển sang kiểm tra thủ công.

## Các mục tiếp theo

| Mục | Điều kiện hoàn thành |
|---|---|
| 2 · OCR | Chạy OCR ảnh thật, lưu tọa độ chữ và giải thích lỗi qua benchmark CER. |
| 3 · PyTorch | Tự viết vòng huấn luyện nhận dạng chữ số và nạp lại checkpoint. |
| 4 · Hugging Face và prompt | Đo prompt và rule trên cùng tập hóa đơn có nhãn. |
| 5 · Fine-tuning | Tạo cặp OCR–JSON, chạy SFT với LoRA và QLoRA, nạp adapter và đo độ chính xác từng trường cùng VRAM. |
| 6 · Serving | Phục vụ qua API và đo p95 latency, throughput và bộ nhớ. |
| 7 · Production | Đóng gói Docker, kiểm tra trace và diễn tập rollback. |
| 8 · Portfolio | Chạy lại từ bản clone mới và công bố số liệu đo được. |

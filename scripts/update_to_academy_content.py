#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script to update Simon Center Second Brain (index.html & dashboard.html)
from Clinic Patient Recruitment to Chiropractic Academy / Training Enrollment (DISC Standard).
"""

import re
import json

# 21 Posts Data for 7 Days
plan7_days_academy = [
    {
        "day": 1,
        "date": "14/09",
        "dayName": "Thứ Hai",
        "theme": "Đánh Thức Nỗi Sợ & Sự Thật Về 'Bẻ Khớp Dạo'",
        "status": "Đã xuất bản (day1.txt)",
        "posts": [
            {
                "time": "Sáng 08:00",
                "channel": "fb_personal",
                "channelName": "FB Cá Nhân",
                "voice": "voice1",
                "voiceName": "Giọng 1 (Thấu cảm)",
                "title": "Tại sao 80% người học nắn chỉnh 2-3 ngày về nhà đều run tay không dám làm trên bệnh nhân thật?",
                "cta": "Để lại bình luận hoặc điền form nhận cẩm nang kiểm tra an toàn y khoa",
                "content": """Hôm qua, tôi ngồi trò chuyện với một bạn kỹ thuật viên Vật lý trị liệu 29 tuổi. Bạn ấy vừa bỏ ra gần 20 triệu để tham gia một khóa học nắn chỉnh cột sống cấp tốc 2 ngày cuối tuần tại một khách sạn lớn.

Bạn nhìn tôi, thở dài bảo:
"Hôm học ở hội trường đông cả trăm người, thầy cầm đầu bạn học viên bẻ 'rắc rắc' nghe sướng tai lắm anh. Em cũng lên thực hành thử, bẻ được vài cái nghe kêu to, thầy vỗ vai khen có khiếu. Nhưng thứ Hai vừa rồi, có một bệnh nhân nữ 45 tuổi bị đau thắt lưng đến phòng khám em. Khi đặt tay lên lưng chị ấy, tự nhiên tim em đập thình thịch, hai bàn tay run bần bật anh ạ. Em chợt nhận ra: Em hoàn toàn không biết đĩa đệm chị ấy có bị rách không, đốt sống có bị loãng xương hay trượt không. Em sợ nếu lỡ tay vặn mạnh một cái mà bệnh nhân bị liệt thì đời em coi như xong..."

Câu chuyện của bạn khiến tôi day dứt khôn nguôi, bởi vì đó là tâm trạng chung của hơn 80% người sau khi học các lớp nắn chỉnh ngắn ngày hiện nay.

Chúng ta đang bị mạng xã hội đánh lừa bởi những tiếng kêu giòn tai! Người ta dạy bạn "chiêu thức" để tạo ra tiếng rắc, nhưng người ta không dạy bạn:
1. Cách đọc phim X-quang để thấy rõ cấu trúc giải phẫu bên dưới lớp da.
2. Cách sờ nắn chẩn đoán động (Motion Palpation) để tìm đúng đốt kẹt (Hypomobile), và quan trọng nhất:
3. Nắm vững lằn ranh "Cảnh báo đỏ" (Red Flags): Khi nào TUYỆT ĐỐI KHÔNG ĐƯỢC PHÉP NẮN.

Trong ngành y, sự sợ hãi khi thiếu kiến thức là phản xạ sinh tồn lành mạnh. Nhưng nếu bạn muốn biến nỗi sợ thành sự tự tin vững chãi của một chuyên gia, bạn bắt buộc phải học từ nền tảng chẩn đoán gốc rễ thay vì học ngọn.

Simon Center xây dựng chương trình đào tạo Chiropractic chuẩn y khoa kế thừa từ DISC Academy (Đức) với sứ mệnh duy nhất: Giúp bạn nắm vững cơ chế an toàn tuyệt đối, đọc thấu phim X-quang và tự tin trị liệu trọn đời mà không bao giờ phải run tay.

👉 Điền form nhận Cẩm nang Tầm soát An toàn Y khoa & Lộ trình đào tạo chuẩn Đức tại đây: [ĐIỀN FORM TẠI ĐÂY]"""
            },
            {
                "time": "Trưa 11:30",
                "channel": "tiktok_reels",
                "channelName": "TikTok / Reels",
                "voice": "voice2",
                "voiceName": "Giọng 2 (Học thuật)",
                "title": "Cú bẻ khớp 'răng rắc' trên TikTok vs Kỹ thuật nắn HVLA chuẩn Đức: Điểm khác biệt nguy hiểm",
                "cta": "Bấm link bio nhận Cẩm nang Tầm soát Cột Sống chuẩn y khoa",
                "content": """[HÌNH ẢNH / VISUAL VIDEO 60S]:
- 00:00 - 00:05: Đoạn clip bẻ cổ giật cục trên TikTok chèn âm thanh giòn tan. Text: "Bạn đang học chữa bệnh hay học làm xiếc?"
- 00:05 - 00:30: Mô hình đốt sống cổ và động mạch đốt sống (Vertebral Artery). Minh họa hiện tượng vặn xoắn quá đà.
- 00:30 - 00:60: Giảng viên Simon Center thao tác cú nắn HVLA êm ái, biên độ cực ngắn, bệnh nhân mỉm cười thư giãn.

[LỜI THOẠI / VOICE-OVER]:
Dừng lại lướt TikTok 3 giây! Nếu bạn đang có ý định đi học nắn chỉnh xương khớp, hãy nghe kỹ điều này trước khi quá muộn!

Rất nhiều người lầm tưởng: Tiếng "rắc" càng to chứng tỏ tay nghề càng cao.
Sai hoàn toàn từ Nguyên lý gốc (First Principles)!

1. Tiếng kêu đó là gì?
Đó chỉ là hiện tượng sủi bọt khí (Cavitation) — khi dịch khớp bị kéo căng đột ngột, áp lực âm giải phóng bóng khí Nitơ. Bất kỳ ai dùng lực thô bạo vặn xoắn cổ cũng có thể tạo ra tiếng kêu, kể cả người không học y!

2. Sự nguy hiểm chết người của "bẻ khớp dạo":
Khi bạn vặn xoắn toàn bộ vùng cổ biên độ lớn, bạn đang nắn vào "đốt lỏng" (Hypermobile) — nơi dây chằng đã bị giãn. Làm nhiều lần sẽ gây mất vững cột sống vĩnh viễn, rách động mạch đốt sống dẫn đến đột quỵ!

3. Kỹ thuật nắn HVLA chuẩn Đức từ DISC Academy khác biệt thế nào?
- HVLA là High Velocity, Low Amplitude: Tốc độ cao nhưng Biên độ cực ngắn (chỉ 2-3 milimet).
- Không xoay vặn thô bạo: Lực đi thẳng vào đốt sống bị kẹt (Hypomobile), đưa khớp về trục giải phẫu mà bệnh nhân chưa kịp gồng sợ thì khớp đã êm ru!

Đừng làm thợ bẻ khớp dạo. Hãy trở thành chuyên gia nắn chỉnh chuẩn y khoa!
Bấm ngay link bio để nhận tài liệu phân tích cơ sinh học nắn chỉnh an toàn nhé!"""
            },
            {
                "time": "Tối 20:00",
                "channel": "fanpage",
                "channelName": "Fanpage Học Viện",
                "voice": "voice2",
                "voiceName": "Giọng 2 (Tư duy sự nghiệp)",
                "title": "Nghề trị liệu cơ xương khớp: Bạn muốn cả đời làm thợ xoa bóp tay chân hay trở thành Chuyên gia định vị gốc bệnh?",
                "cta": "Nhận lộ trình nâng tầm tay nghề tại link form bên dưới",
                "content": """[BẠN MUỐN CẢ ĐỜI LÀM THỢ XOA BÓP DÙNG SỨC HAY TRỞ THÀNH CHUYÊN GIA ĐỊNH VỊ GỐC BỆNH?]

Đây là một câu hỏi thẳng thắn, có phần gai góc, nhưng tôi muốn dành riêng cho các anh chị em đang làm Kỹ thuật viên Vật lý trị liệu, Y học cổ truyền, Spa dưỡng sinh hay Huấn luyện viên thể hình (PT).

Hãy nhìn lại một ngày làm việc của bạn:
- Một ngày tiếp 4 - 5 ca xoa bóp, giãn cơ, bấm huyệt, mỗi ca kéo dài 60 - 90 phút.
- Bạn dùng hết sức lực của ngón tay, cổ tay, bờ vai để đè, miết, ấn cho khách.
- Tối về đến nhà, lưng bạn còng xuống, các khớp ngón tay ê buốt, người mệt lử không còn chút năng lượng nào cho gia đình.
- Và mức thù lao nhận lại: Vài chục đến một vài trăm ngàn cho mỗi buổi làm việc kiệt sức!

Bạn có từng tự hỏi: Đôi bàn tay và cột sống của bạn sẽ chịu đựng được cường độ lao động tay chân này thêm bao nhiêu năm nữa? 3 năm? 5 năm? Rồi sau đó thì sao?

Sự khác biệt giữa một "Người thợ xoa bóp" và một "Chuyên gia trị liệu Chiropractic":
1. Người thợ dùng SỨC BẮP TAY — Chuyên gia dùng TRÍ TUỆ GIẢI PHẪU & NGUYÊN LÝ CƠ SINH HỌC.
2. Người thợ chữa phần ngọn (đau đâu xoa bóp đấy, 3 hôm khách đau lại) — Chuyên gia đọc phim X-quang, tìm ra đúng đốt lệch tiên phát (Primary Subluxation) để xử lý triệt để căn nguyên.
3. Người thợ mất 60 phút còng lưng — Chuyên gia chỉ cần 10 - 15 phút nắn chỉnh chuẩn xác, êm ái, mang lại giá trị điều trị 500.000đ - 1.000.000đ/ca.

Nâng cấp tay nghề không chỉ là học thêm một kỹ thuật mới, mà là bước ngoặt thay đổi hoàn toàn vị thế nghề nghiệp, bảo vệ sức khỏe của chính bạn và gia tăng thu nhập bền vững.

Simon Center đồng hành cùng bạn trên hành trình chuyển hóa này với chương trình đào tạo chuẩn Đức DISC Academy.
👉 Nhận bản đồ lộ trình chuyển đổi sự nghiệp tại đây: [ĐIỀN FORM TẠI ĐÂY]"""
            }
        ]
    },
    {
        "day": 2,
        "date": "15/09",
        "dayName": "Thứ Ba",
        "theme": "Vũ Khí Tối Thượng: Đọc Phim X-Quang & Tìm Đốt Lệch Tiên Phát",
        "status": "Kế hoạch sẵn sàng",
        "posts": [
            {
                "time": "Sáng 08:00",
                "channel": "fanpage",
                "channelName": "Fanpage Học Viện",
                "voice": "voice2",
                "voiceName": "Giọng 2 (Học thuật DISC)",
                "title": "Đau thắt lưng nhưng đốt lệch tiên phát lại nằm ở cổ: Bài học xương máu từ DISC Academy Đức",
                "cta": "Đăng ký tham gia Workshop giải mã bản đồ X-quang Full-Spine",
                "content": """[ĐAU THẮT LƯNG NHƯNG GỐC BỆNH LẠI NẰM Ở CỔ: BÀI HỌC CƠ SINH HỌC XƯƠNG MÁU TỪ ĐỨC]

Trong các lớp học nắn chỉnh cơ học thông thường, học viên được dạy công thức cực kỳ đơn giản: "Bệnh nhân kêu đau thắt lưng L4-L5 -> đè lưng ra nắn. Bệnh nhân kêu mỏi cổ C5-C6 -> bẻ cổ kêu rắc rắc".

Nếu trị liệu cơ thể người đơn giản như vậy, tại sao có những bệnh nhân đau lưng dưới đi nắn chỉnh cả chục lần mà chỉ đỡ được 2 ngày rồi đau nhức trở lại?

Câu trả lời nằm ở nguyên lý cơ sinh học toàn thể (Full-Spine Biomechanics) mà các giảng viên tại DISC Academy (Đức) luôn khắc sâu cho học viên:

1. Nguyên lý phản chiếu Lovett Reactor:
Cột sống là một chuỗi động học thống nhất. Cổ và thắt lưng luôn vận động bù trừ cho nhau theo cặp:
- Đốt đội C1 phản chiếu với L5.
- Đốt trục C2 phản chiếu với L4.
- C3 phản chiếu với L3.
Khi đốt C1-C2 bị xoay lệch trục, hộp sọ bị nghiêng, não bộ sẽ lập tức phát tín hiệu bắt khung chậu và đốt sống L4-L5 vặn xoắn theo chiều ngược lại để giữ tầm mắt luôn thăng bằng!

2. Đốt lệch tiên phát (Primary) vs Đốt bù trừ (Compensatory):
Đốt L4-L5 đau buốt thực chất chỉ là "nạn nhân gánh tội thay" cho góc lệch ở đốt cổ C1-C2. Nếu bạn chỉ nhăm nhe đè lưng bệnh nhân ra nắn, bạn đang nắn vào đốt bù trừ. Hệ thần kinh sẽ lập tức bắt cơ lưng co cứng trở lại chỉ sau 48 tiếng!

3. Giải pháp:
Chỉ khi đặt tấm phim X-quang Full-Spine lên hộp đèn, đo đạc chính xác góc nghiêng xương chậu, kẻ đường trục George's Line ở cổ và giải phóng đúng đốt lệch tiên phát C1, chiếc thắt lưng mới tự động nhả áp lực và hồi phục vĩnh viễn!

Đây chính là tư duy "Specific" (Chuẩn xác đích thực) tạo nên đẳng cấp của một Master Chiropractic.
👉 Đăng ký tham gia buổi Workshop Trực Tuyến: 'Giải mã bản đồ X-quang cột sống Full-Spine cùng Giảng viên DISC' tại đây: [ĐIỀN FORM TẠI ĐÂY]"""
            },
            {
                "time": "Trưa 11:30",
                "channel": "group_community",
                "channelName": "Group Cộng Đồng YHCT & Trị Liệu",
                "voice": "voice1",
                "voiceName": "Giọng 1 (Chia sẻ nghề)",
                "title": "Từ ngày biết đọc phim X-quang, tôi không còn phải 'đoán mò' hay nắn chữa cháy theo chỗ đau",
                "cta": "Nhận miễn phí E-book hướng dẫn 5 bước đọc phim X-quang cột sống",
                "content": """Chào các anh chị em đồng nghiệp trong nhóm,

Tôi từng có những năm tháng làm nghề trị liệu trong sự hoang mang tột độ. Mỗi lần bệnh nhân bước vào, chỉ vào vùng thắt lưng bảo "chỗ này buốt quá em ơi", tôi lại dùng tay sờ nắn, day miết và cố gắng làm hết sức mình. Bệnh nhân đỡ thì mừng, bệnh nhân bảo không đỡ thì đêm về tôi mất ngủ, tự hỏi mình đã làm sai ở đâu.

Cảm giác bất lực nhất của người làm nghề y là: PHẢI ĐOÁN MÒ!

Mọi thứ chỉ thực sự thay đổi 180 độ khi tôi được đào tạo bài bản phương pháp đọc phim X-quang cột sống theo tiêu chuẩn Đức.

Lần đầu tiên, tôi không còn nhìn cơ thể qua lớp da thịt bên ngoài. Khi bệnh nhân mang phim chụp đến:
- Tôi chỉ cho họ thấy rõ đốt L4 đang trượt ra sau 2.5mm so với L5.
- Tôi chỉ cho họ thấy gai xương ở lỗ tiếp hợp đang chèn rễ thần kinh tọa.
- Tôi giải thích cặn kẽ vì sao họ cúi thì đau mà ưỡn lưng lại dễ chịu.

Các bạn có biết khoảnh khắc đó tuyệt vời thế nào không?
Bệnh nhân nhìn vào mắt tôi với sự tin tưởng tuyệt đối. Họ không còn coi tôi là một người thợ xoa bóp, mà họ tôn trọng tôi như một Chuyên gia thực thụ. Và quan trọng nhất: Tôi biết chính xác mình cần đặt lực nắn vào đâu, góc bao nhiêu độ, và chỗ nào TUYỆT ĐỐI KHÔNG ĐƯỢC CHẠM VÀO.

Biết đọc phim X-quang chính là chiếc "chìa khóa vàng" mở toang cánh cửa tự tin và nâng tầm giá trị cho bất kỳ ai làm nghề trị liệu cơ xương khớp.

Tuần này, Simon Center xin gửi tặng các đồng nghiệp cuốn E-book độc quyền: "Hướng dẫn 5 bước đọc phim X-quang Cột sống cho Kỹ thuật viên trị liệu". Anh chị để lại thông tin tại link bên dưới để nhận tài liệu nhé ạ!
👉 [NHẬN E-BOOK X-QUANG MIỄN PHÍ TẠI ĐÂY]"""
            },
            {
                "time": "Tối 20:00",
                "channel": "fb_personal",
                "channelName": "FB Cá Nhân",
                "voice": "voice1",
                "voiceName": "Giọng 1 (Chuyên gia chia sẻ)",
                "title": "3 góc đo trượt đốt sống trên phim X-quang mà một Chiropractor chuyên nghiệp bắt buộc phải nắm trong 30 giây",
                "cta": "Đăng ký nhận thông tin khóa đào tạo đọc phim X-quang thực chiến",
                "content": """Một người thợ nắn chỉnh thông thường nhìn tấm phim X-quang chỉ thấy "xương trắng trắng, đen đen". Nhưng một Chiropractor chuẩn y khoa nhìn tấm phim X-quang giống như một kỹ sư nhìn bản vẽ kết cấu của một tòa nhà chọc trời.

Trong vòng 30 giây đầu tiên cầm phim, có 3 góc đo then chốt bạn bắt buộc phải đọc được:

1. Đường thẳng George (George's Line) — Thước đo độ vững đốt sống:
Kẻ một đường cong liên tục men theo bờ sau các thân đốt sống cổ hoặc thắt lưng. Nếu đường này bị gãy khúc tại bất kỳ vị trí nào dù chỉ 2mm, đó là dấu hiệu của Trượt đốt sống (Spondylolisthesis). Nếu bạn không nhận ra mà nắn lực mạnh vào đây, bạn có thể làm rách bao khớp và chèn ép tủy sống ngay lập tức!

2. Góc nghiêng xương cùng (Sacral Base Angle):
Góc hợp bởi mặt trên xương cùng S1 và phương ngang. Góc chuẩn là 38 - 42 độ. Nếu góc này tăng trên 45 độ (Tăng ưỡn thắt lưng), áp lực cơ học dồn lên đĩa đệm L5-S1 tăng gấp 3 lần! Nắn chỉnh thắt lưng mà không phục hồi góc nghiêng xương chậu thì bệnh nhân sẽ tái phát suốt đời.

3. Chiều cao đĩa đệm tương đối (Disc Space Ratio):
So sánh khoảng cách khe khớp giữa đốt sống nghi ngờ với đốt sống liền kề. Khoảng gian đốt hẹp trên 30% kèm xơ đặc xương dưới sụn là bằng chứng đĩa đệm đã thoái hóa mất nước giai đoạn 2.

Đôi mắt đọc được phim X-quang chính là ranh giới phân định đẳng cấp giữa một người "bẻ khớp dạo" và một Chuyên gia nắn chỉnh quốc tế.

Tại khóa học Chiropractic Simon Center, học viên được thực hành phân tích trực tiếp trên hơn 200 bộ phim X-quang ca bệnh thật cho đến khi thành thạo như phản xạ tự nhiên.
👉 Tìm hiểu khung chương trình đào tạo chuyên sâu tại đây: [ĐIỀN FORM TẠI ĐÂY]"""
            }
        ]
    },
    {
        "day": 3,
        "date": "16/09",
        "dayName": "Thứ Tư",
        "theme": "An Toàn Tuyệt Đối: Nguyên Tắc Bốn Chữ CẤM & Cảnh Báo Đỏ (Red Flags)",
        "status": "Kế hoạch sẵn sàng",
        "posts": [
            {
                "time": "Sáng 08:00",
                "channel": "fanpage",
                "channelName": "Fanpage Học Viện",
                "voice": "voice2",
                "voiceName": "Giọng 2 (Nguyên lý Y đức)",
                "title": "Biết khi nào TUYỆT ĐỐI KHÔNG ĐƯỢC NẮN còn quan trọng gấp trăm lần học cách nắn!",
                "cta": "Đăng ký giữ chỗ khóa đào tạo an toàn trọn đời cùng Simon Center",
                "content": """[TRONG NẮN CHỈNH: BIẾT KHI NÀO CẤM NẮN QUAN TRỌNG GẤP TRĂM LẦN HỌC CÁCH NẮN!]

Lời thề Hippocrates có một nguyên tắc tối thượng mà bất kỳ ai bước chân vào ngành y đều phải khắc cốt ghi tâm: "Primum non nocere" — Trước hết, không làm tổn hại người bệnh.

Tôi từng chứng kiến những học viên sau các khóa học bẻ khớp ngắn ngày mang tâm lý "ảo tưởng sức mạnh". Vừa học được vài miếng võ vặn cổ, vặn lưng, gặp ai cũng đòi đè ra nắn: Từ cụ già 70 tuổi loãng xương, bạn trẻ thoát vị đĩa đệm rách bao xơ cấp tính, cho đến người bị dị dạng mạch máu não!

Đó không phải là trị liệu. Đó là sự liều lĩnh đến vô nhân đạo!

Tại Simon Center (kế thừa tiêu chuẩn DISC Academy Đức), điều đầu tiên chúng tôi dạy học viên KHÔNG PHẢI LÀ KỸ THUẬT NẮN. Điều đầu tiên học viên bắt buộc phải học và thi đỗ là: BỘ LỌC CẢNH BÁO ĐỎ (RED FLAGS) — Danh mục các trường hợp TUYỆT ĐỐI CHỐNG CHỈ ĐỊNH:

1. Thoát vị đĩa đệm thể tự do / Rách vòng sợi bao xơ cấp tính (Cấm nắn vặn xoắn lực mạnh).
2. Trượt đốt sống độ 3, độ 4 mất vững cấu trúc.
3. Loãng xương nặng (T-score < -2.5) — Cú nắn lực mạnh có thể làm xẹp lún thân đốt sống hoặc gãy xương sườn người bệnh!
4. Thiểu năng tuần hoàn động mạch đốt sống thân nền (Hội chứng VBI) — Cú bẻ cổ thô bạo có thể gây tắc mạch và đột quỵ tại chỗ.
5. Lao cột sống, u tủy, viêm cột sống dính khớp giai đoạn tiến triển.

Người bình thường nhìn vào chỉ thấy kỹ thuật nắn hào nhoáng. Nhưng người làm nghề chân chính hiểu rằng: Bản lĩnh của một người thầy thuốc nằm ở chỗ BIẾT TỪ CHỐI VÀ BIẾT KHI NÀO CẦN CHUYỂN TUYẾN BỆNH VIỆN.

Một ca nắn thành công mang lại cho bạn vài trăm ngàn. Nhưng một ca tai biến do nắn ẩu vào ca chống chỉ định sẽ hủy hoại toàn bộ sự nghiệp và danh dự cả đời của bạn!

Simon Center cam kết đào tạo bạn trở thành chuyên gia nắn chỉnh an toàn trọn đời.
👉 Đăng ký tư vấn chương trình đào tạo chuẩn y khoa tại đây: [ĐIỀN FORM TẠI ĐÂY]"""
            },
            {
                "time": "Trưa 11:30",
                "channel": "tiktok_reels",
                "channelName": "TikTok / Reels",
                "voice": "voice2",
                "voiceName": "Giọng 2 (Tình huống cảnh báo)",
                "title": "5 dấu hiệu 'Cờ Đỏ' (Red Flags) nếu bạn cố tình nắn sẽ gây tai biến y khoa nghiêm trọng",
                "cta": "Nhận ngay bảng checklist 10 Cờ Đỏ lâm sàng tại link bio",
                "content": """[VIDEO REELS/TIKTOK 60S: 5 DẤU HIỆU CỜ ĐỎ CẤM NẮN CHỈNH!]

[VISUAL]:
- Chuyên gia đứng trước mô hình cột sống, vẻ mặt nghiêm túc, giơ bảng cảnh báo nguy hiểm màu đỏ.
- Text: "Nếu gặp 5 dấu hiệu này, dừng tay lại ngay lập tức!"

[VOICE-OVER]:
Nếu bạn đang làm nghề nắn chỉnh, hãy lưu video này lại ngay để cứu lấy sự nghiệp của bạn!
Đây là 5 dấu hiệu "Cờ Đỏ" (Red Flags) mà nếu bạn cố tình bẻ khớp, tai biến y khoa có thể xảy ra ngay trên bàn nắn:

Số 1: Hội chứng chùm đuôi ngựa (Cauda Equina) — Bệnh nhân đau lưng kèm tê bì mất cảm giác vùng yên ngựa (quanh hậu môn) và bí tiểu tiện. Đây là cấp cứu ngoại khoa, nắn vào là liệt vĩnh viễn!
Số 2: Đau tăng dữ dội về đêm và sụt cân không rõ nguyên nhân — Cảnh báo khối u tủy hoặc di căn xương.
Số 3: Chóng mặt, rung giật nhãn cầu, ngất xỉu khi quay đầu (Test DeKleyn dương tính) — Dấu hiệu chèn ép động mạch đốt sống cổ, tuyệt đối cấm bẻ cổ!
Số 4: Đang dùng thuốc chống đông máu hoặc Corticoid kéo dài — Nguy cơ xuất huyết khoang ngoài màng cứng và giòn xương.
Số 5: Sốt cao kèm đau cột sống dữ dội — Nghi ngờ viêm đĩa đệm đốt sống nhiễm khuẩn.

Làm nghề y, an toàn của người bệnh là mạng sống của chính bạn!
Bấm ngay link bio để tải về trọn bộ Checklist 10 Cờ Đỏ lâm sàng chuẩn quốc tế nhé!"""
            },
            {
                "time": "Tối 20:00",
                "channel": "fb_personal",
                "channelName": "FB Cá Nhân",
                "voice": "voice3",
                "voiceName": "Giọng 3 (Xử lý từ chối - Đạo đức)",
                "title": "Khách hỏi: 'Sao bên kia học phí nắn chỉnh chỉ vài triệu mà bên Simon Center học phí lại cao hơn?'",
                "cta": "Đăng ký sớm nhận ưu đãi đặc quyền khóa đào tạo chuẩn DISC",
                "content": """Hôm qua, có một bạn làm quản lý phòng tập gym nhắn tin hỏi tôi rất thẳng thắn:
"Anh ơi, em thấy trên mạng có nhiều chỗ dạy nắn chỉnh xương khớp chỉ 3 - 5 triệu, học 2 ngày là cấp chứng nhận làm nghề luôn. Sao khóa học bên Simon Center học phí lại cao hơn vậy anh?"

Tôi rất thích những câu hỏi sòng phẳng như vậy, và tôi đã chia sẻ với bạn ấy câu trả lời từ tận đáy lòng:

"Em ơi, trong kinh doanh, cái gì cũng có cái giá của nó. Nhưng trong ngành y và sức khỏe con người, sự chênh lệch về học phí phản ánh chính xác sự khác biệt giữa 'RỦI RO TAI BIẾN' và 'SỰ AN TOÀN TRỌN ĐỜI'.

Một khóa học vài triệu dạy dồn dập 2 ngày tại hội trường đông người thường chỉ dạy em vài thao tác bẻ khớp thô bạo. Họ không dạy em cách đọc phim X-quang, không dạy em tầm soát Cảnh báo đỏ (Red Flags), không có bài tập rèn lực tại nhà và sau 2 ngày là 'đem con bỏ chợ', không ai chịu trách nhiệm cùng em.

Em thử nghĩ xem: Khi em hành nghề, rủi ro lớn nhất không phải là học phí đắt hay rẻ.
Rủi ro lớn nhất là nếu em lỡ tay nắn sai vào một ca loãng xương làm gãy xương sườn bệnh nhân, hay bẻ cổ làm rách mạch máu não của họ... Lúc đó, tiền viện phí bồi thường, sự dằn vặt lương tâm và uy tín danh dự cả đời của em liệu vài triệu tiền học phí kia có bù đắp nổi không?

Tại Simon Center:
- Em được học phương pháp Specific chuẩn Đức từ DISC Academy.
- Em được học đọc phim X-quang chuyên sâu để định vị chính xác đốt lệch.
- Em được thi test qua môn sàng lọc bệnh nhân an toàn 100%.
- Em được trang bị hệ thống E-Learning 4K xem lại trọn đời, bài tập Micro-drills rèn phản xạ và có hội đồng chuyên môn hội chẩn ca bệnh khó cùng em 24/7.

Với mức đầu tư này, khi ra nghề em chỉ cần tiếp nhận 5-6 bệnh nhân điều trị là đã thu hồi hoàn toàn chi phí học. Nhưng giá trị an toàn, sự tự tin và danh tiếng chuyên gia sẽ theo em suốt cả cuộc đời."

Bạn ấy im lặng một lúc rồi bảo: "Em hiểu rồi anh. Cho em đăng ký phỏng vấn khóa tới nhé anh!"

Lựa chọn thuộc về bạn. Hãy đầu tư cho sự nghiệp của mình bằng sự vững chãi và tử tế nhất.
👉 Đăng ký nhận thông tin tuyển sinh khóa mới tại đây: [ĐIỀN FORM TẠI ĐÂY]"""
            }
        ]
    },
    {
        "day": 4,
        "date": "17/09",
        "dayName": "Thứ Năm",
        "theme": "Phương Pháp Sư Phạm Khác Biệt: Micro-Drills & Kỹ Thuật Thả Lỏng Body Drop",
        "status": "Kế hoạch sẵn sàng",
        "posts": [
            {
                "time": "Sáng 08:00",
                "channel": "fb_personal",
                "channelName": "FB Cá Nhân",
                "voice": "voice2",
                "voiceName": "Giọng 2 (Khoa học cơ sinh học)",
                "title": "Nắn chỉnh không cần gồng cơ bắp tay: Bí mật công thức xung lực F·Δt = m·Δv giúp KTV nữ 45kg vẫn nắn êm ru",
                "cta": "Trải nghiệm phương pháp rèn phản xạ Body Drop tại Simon Center",
                "content": """Nhiều người nghĩ rằng: Muốn làm Chiropractor nắn chỉnh xương khớp thì người phải to cao, cơ bắp cuồn cuộn như lực sĩ thể hình thì mới đủ sức nắn!

Đó là một trong những hiểu lầm tai hại nhất bắt nguồn từ lối nắn thô bạo.

Dưới góc độ vật lý cơ sinh học (Biomechanics), kỹ thuật nắn HVLA (High Velocity, Low Amplitude) không phụ thuộc vào sức mạnh của bắp tay, mà phụ thuộc vào XUNG LỰC và TỐC ĐỘ.

Hãy nhìn vào định luật 2 Newton:
F · Δt = m · Δv
(Lực tác động nhân với khoảng thời gian bằng khối lượng nhân với độ biến thiên vận tốc).

Để tạo ra một lực đẩy đủ để giải phóng một đốt sống bị kẹt:
- Người nắn dạo cố tăng lực F bằng cách gồng cứng bắp tay và vai -> Kết quả là thời gian Δt bị kéo dài (chậm chạp), bệnh nhân bị đau, cơ bắp phản xạ gồng chống lại, gây nguy cơ chấn thương!
- Chuyên gia chuẩn Đức làm ngược lại: Thu hẹp tối đa thời gian tác động Δt (cực nhanh, chỉ 0.05 giây) bằng kỹ thuật THẢ LỎNG TRỌNG LƯỢNG CƠ THỂ (Body Drop).

Kỹ thuật Body Drop là gì?
Hai cánh tay của người nắn hoàn toàn thư giãn, chỉ đóng vai trò truyền dẫn lực. Toàn bộ xung lực được tạo ra từ việc thả rơi trọng lượng cơ thể (Body Weight Drop) trong chớp mắt. 

Chính vì vậy, tại Simon Center, những kỹ thuật viên nữ chỉ nặng 45 - 48kg vẫn có thể thực hiện cú nắn thắt lưng cho một vận động viên nặng 90kg một cách cực kỳ nhẹ nhàng, êm ái mà bệnh nhân chưa kịp cảm nhận sợ hãi thì khớp đã được giải phóng êm ru!

Học đúng nguyên lý, bạn sẽ làm nghề bằng sự thanh thoát chứ không phải bằng sự vất vả cơ bắp.
👉 Khám phá phương pháp huấn luyện Body Drop tại đây: [ĐIỀN FORM TẠI ĐÂY]"""
            },
            {
                "time": "Trưa 11:30",
                "channel": "group_community",
                "channelName": "Group Kỹ Thuật Viên Trị Liệu",
                "voice": "voice1",
                "voiceName": "Giọng 1 (Sư phạm đổi mới)",
                "title": "Tại sao học nắn chỉnh qua video thông thường là 'ném tiền qua cửa sổ' nếu không có bài tập rèn phản xạ tại nhà?",
                "cta": "Đăng ký nhận thử 1 Module Micro-Drill rèn lực tại nhà miễn phí",
                "content": """Chào các anh chị em,

Thời gian gần đây, tôi thấy rất nhiều anh chị em mua các khóa học nắn chỉnh online trên mạng — chỉ là các video quay lại cảnh giảng viên nắn trên người thật, xem xong rồi để đó. Hầu hết mọi người xem xong đều thừa nhận: "Lúc xem video thì thấy dễ lắm, nhưng khi bảo tự làm thì chịu chết, tay chân cứng đờ không biết đặt lực thế nào!"

Tại sao lại như vậy?
Bởi vì nắn chỉnh là môn TRÍ NHỚ CƠ BẮP (Muscle Memory) và PHẢN XẠ THẦN KINH CƠ. Bạn không thể học bơi chỉ bằng cách ngồi xem video người khác bơi!

Tại DISC Academy (Đức) và Simon Center, chúng tôi giải quyết bài toán này bằng hệ thống độc quyền: MICRO-DRILLS (Bài tập rèn luyện phản xạ vi mô tại nhà).

Micro-drills hoạt động như thế nào?
Thay vì bắt bạn đè người thật ra nắn ngay (vừa nguy hiểm vừa sợ hãi), kỹ thuật nắn được chia nhỏ thành từng phản xạ đơn lẻ:
1. Drill rèn điểm tiếp xúc (Contact Point): Tập cảm giác tay đặt đúng mỏm gai, mỏm ngang trên mô hình giải phẫu.
2. Drill hướng vector lực (Line of Drive): Tập hướng rơi của trọng tâm cơ thể trên bóng cao su chuyên dụng.
3. Drill tốc độ thả lỏng (Speed & Relaxation): Tập tạo xung lực nhanh dưới 0.05 giây trên đệm lò xo Drop Pad.

Bạn tập luyện các bài drill này tại nhà mỗi ngày 15 phút. Khi phản xạ cơ bắp đã thành thục, việc bạn chạm tay vào bệnh nhân thật sẽ diễn ra tự nhiên, chuẩn xác và không hề có cảm giác sợ hãi hay run rẩy.

Học nắn chỉnh online hoàn toàn có thể làm chủ tay nghề xuất sắc — nếu và chỉ nếu bạn có một phương pháp sư phạm rèn phản xạ đúng đắn!
👉 Trải nghiệm thử 1 Module Micro-Drill độc quyền tại đây: [ĐĂNG KÝ HỌC THỬ MIỄN PHÍ]"""
            },
            {
                "time": "Tối 20:00",
                "channel": "fanpage",
                "channelName": "Fanpage Học Viện",
                "voice": "voice1",
                "voiceName": "Giọng 1 (Câu chuyện học viên)",
                "title": "Câu chuyện một KTV Vật lý trị liệu 30 tuổi: 'Cổ tay em từng đau nhức vì dùng lực thô bạo, cho đến khi học được cú thả lỏng Body Drop chuẩn Đức'",
                "cta": "Đăng ký tham gia khóa đào tạo chuyên sâu cùng Simon Center",
                "content": """Chiều nay, tôi nhận được tin nhắn từ bạn Tuấn — một cựu học viên KTV Phục hồi chức năng khóa 3 tại Simon Center.

Tuấn nhắn: "Anh ơi, hôm nay em tiếp 6 ca nắn chỉnh mà tay vẫn nhẹ bẫng. Nghĩ lại thời điểm cách đây 1 năm mà em thấy mình may mắn quá anh ạ!"

Trước khi đến với Simon Center, Tuấn từng làm KTV cho một phòng khám tư. Hằng ngày bạn phải gồng hết cơ bắp tay để bẻ lưng, kéo giãn cho bệnh nhân. Hậu quả là sau 2 năm làm nghề, cổ tay phải của bạn bị viêm gân bao hoạt dịch de Quervain đau nhức dữ dội, ngón tay cái run rẩy không cầm nổi bát cơm. Bác sĩ cảnh báo nếu tiếp tục dùng lực tay như vậy, bạn sẽ phải từ bỏ nghề trị liệu trước tuổi 35.

Tuấn đến với khóa học của Simon Center trong tâm thế người tìm đường cứu lấy sự nghiệp của chính mình. 

Tại đây, bạn được "tẩy não" toàn bộ thói quen dùng lực bắp tay cũ. Giảng viên DISC chỉnh cho bạn từng tư thế đứng (Stance), cách hạ trọng tâm vùng chậu và dùng trọng lực rơi tự do (Body Drop) để phát lực.

Tuấn kể: "Buổi đầu tiên thực hành cú Body Drop trên giường nắn, em giật mình vì không ngờ nắn chỉnh lại nhẹ đến thế! Em không hề tốn một chút sức lực nào ở cổ tay, mà khớp đốt sống của người mẫu trượt vào vị trí êm ru. Bệnh nhân còn bảo: Sao thấy êm hơn hẳn mấy lần trước vậy em?"

Làm nghề y cứu người, trước hết phải biết bảo vệ chính thân thể của mình.
Đừng để sự nghiệp của bạn bị cắt ngắn bởi những chấn thương nghề nghiệp không đáng có. Hãy học nắn chỉnh bằng sự thông thái của cơ sinh học công thái học (Ergonomics).
👉 Đăng ký tham gia khóa đào tạo chuyên sâu cùng Simon Center tại đây: [ĐIỀN FORM TẠI ĐÂY]"""
            }
        ]
    },
    {
        "day": 5,
        "date": "18/09",
        "dayName": "Thứ Sáu",
        "theme": "Bài Toán Kinh Tế Phòng Khám & Khả Năng Hoàn Vốn Đầu Tư (High ROI)",
        "status": "Kế hoạch sẵn sàng",
        "posts": [
            {
                "time": "Sáng 08:00",
                "channel": "fanpage",
                "channelName": "Fanpage Học Viện",
                "voice": "voice3",
                "voiceName": "Giọng 3 (Kinh doanh phòng khám)",
                "title": "Bài toán hoàn vốn: Đầu tư khóa học Chiropractic chuẩn y khoa, chỉ cần 5-6 ca bệnh nhân là thu hồi toàn bộ học phí",
                "cta": "Nhận bản kế hoạch tài chính phòng khám trị liệu tại link form",
                "content": """[ĐẦU TƯ KHÓA HỌC CHIROPRACTIC: BAO LÂU THU HỒI VỐN?]

Khi cân nhắc tham gia một chương trình đào tạo chuyên môn cao cấp, câu hỏi thông minh nhất của một người làm nghề thực tế không phải là: "Khóa học này bao nhiêu tiền?", mà là: "KHOẢN ĐẦU TƯ NÀY SẼ ĐEM LẠI LỢI NHUẬN VÀ HOÀN VỐN TRONG BAO LÂU?"

Hãy cùng làm một bài toán tài chính sòng phẳng:

Giả sử bạn đầu tư tham gia Khóa đào tạo toàn diện tại Simon Center (bao gồm trọn gói E-Learning 4K, Micro-drills và Thực hành Cầm tay chỉ việc) với mức học phí khoảng 20 - 30 triệu đồng.

1. Doanh thu của một dịch vụ nắn chỉnh chuẩn y khoa:
- Một buổi xoa bóp giãn cơ thông thường ngoài thị trường: 150.000đ - 250.000đ/buổi.
- Nhưng một buổi nắn chỉnh Chiropractic chuyên sâu (kèm đọc phim X-quang, giải phóng điểm chèn ép cấu trúc chuẩn y khoa): Giá vé niêm yết từ 600.000đ - 1.200.000đ/buổi.

2. Phác đồ điều trị của một bệnh nhân:
Một bệnh nhân đau cột sống mãn tính thường theo phác đồ phục hồi từ 6 đến 10 buổi. 
Tổng doanh thu từ 1 bệnh nhân = 6 buổi x 800.000đ = 4.800.000đ.

3. Điểm hòa vốn (Breakeven Point):
Bạn chỉ cần tiếp nhận:
30.000.000đ / 4.800.000đ ≈ 5 đến 6 BỆNH NHÂN ĐẦU TIÊN!

Chỉ cần 5 đến 6 ca bệnh nhân điều trị thành công, bạn đã thu hồi 100% vốn đầu tư ban đầu của khóa học.
Và điều tuyệt vời nhất là gì?
Kiến thức đọc phim X-quang, kỹ thuật nắn êm ái và sự an toàn y khoa là thứ tài sản nằm trọn vẹn trong đôi tay và khối óc của bạn, không ai có thể lấy đi được. Nó sẽ tiếp tục tạo ra dòng tiền bền vững cho bạn trong suốt 10 năm, 20 năm, thậm chí 30 năm sự nghiệp phía trước!

Đừng coi học phí là chi phí tiêu sản. Đây là khoản đầu tư có tỷ suất sinh lời (ROI) cao nhất trong sự nghiệp của bạn.
👉 Nhận bản kế hoạch tài chính và lộ trình phát triển dịch vụ Chiropractic cho phòng khám/studio tại đây: [ĐIỀN FORM TẠI ĐÂY]"""
            },
            {
                "time": "Trưa 11:30",
                "channel": "tiktok_reels",
                "channelName": "TikTok / Reels",
                "voice": "voice2",
                "voiceName": "Giọng 2 (Bảng so sánh)",
                "title": "So sánh: Khóa học hội trường 2 ngày đông đúc vs Hệ thống E-Learning 4K kèm cặp lâm sàng và xem lại trọn đời",
                "cta": "Xem chi tiết khung chương trình đào tạo tại link bio",
                "content": """[VIDEO REELS/TIKTOK 60S: SO SÁNH 2 MÔ HÌNH ĐÀO TẠO NẮN CHỈNH!]

[VISUAL]:
- Bảng so sánh 2 cột: "Khóa học hội trường 2 ngày" vs "Hệ thống chuẩn Đức Simon Center".
- Slide hình ảnh tương phản: Hội trường đông nghẹt chen lấn vs Góc học E-learning 4K sắc nét và nhóm kèm 1-1 chuyên sâu.

[VOICE-OVER]:
Nếu bạn đang chuẩn bị xuống tiền đi học nắn chỉnh cột sống, hãy xem hết bảng so sánh này để không mất tiền oan!

Mô hình 1: Khóa học hội trường cấp tốc 2 ngày:
- 50 - 100 học viên chen chúc trong một căn phòng.
- Giảng viên biểu diễn trên sân khấu, ở dưới nhìn không rõ góc tay.
- Nhồi nhét lý thuyết trong 48 tiếng -> Về nhà sau 1 tuần quên 80% kiến thức.
- Không có bài test kiểm tra, không ai chỉnh lực tay, học xong là bơ vơ tự chịu trách nhiệm!

Mô hình 2: Hệ sinh thái đào tạo chuẩn Đức tại Simon Center:
- Hệ thống E-Learning 4K đa góc quay: Xem đi xem lại trọn đời trên điện thoại, máy tính bất cứ khi nào cần ôn bài.
- Bài test qua môn lũy tiến sau từng bài: Đảm bảo hiểu chắc 100% cơ chế an toàn và Red Flags mới được mở bài tiếp theo.
- Micro-drills rèn lực rơi tại nhà trước khi chạm người thật.
- Thực hành Cầm tay chỉ việc nhóm nhỏ tối đa 10-12 người cùng Giảng viên DISC.
- Hội đồng chuyên môn hỗ trợ đọc phim hội chẩn ca bệnh khó 24/7!

Đừng học nắn chỉnh kiểu cưỡi ngựa xem hoa. Hãy học để trở thành chuyên gia thực thụ!
Link đăng ký nhận tư vấn lộ trình học ngay ở bio nhé!"""
            },
            {
                "time": "Tối 20:00",
                "channel": "fb_personal",
                "channelName": "FB Cá Nhân",
                "voice": "voice1",
                "voiceName": "Giọng 1 (Đồng hành trọn đời)",
                "title": "Sau khi học xong bạn có bị bỏ rơi? Hệ sinh thái Alumni & Hội đồng chuyên môn hỗ trợ hội chẩn ca bệnh khó 24/7",
                "cta": "Đăng ký sớm gia nhập mạng lưới Alumni Simon Center",
                "content": """Nỗi cô đơn lớn nhất của một người thầy thuốc hay một kỹ thuật viên trị liệu là gì?

Đó là ngày bạn trở về phòng khám của mình, đứng một mình trước một ca bệnh phức tạp. Bệnh nhân cầm tấm phim X-quang có đốt sống trượt vẹo bất thường, kêu đau dữ dội. Bạn nhìn tấm phim, trong đầu ngổn ngang những câu hỏi: Ca này có chỉ định nắn không? Góc đặt tay thế nào cho an toàn? Nếu nắn lỡ có biến chứng thì sao?
Xung quanh bạn không có ai để hỏi, không có ai để hội chẩn cùng. Cảm giác bất lực và đơn độc ấy thật sự rất đáng sợ!

Chính vì từng thấu hiểu sâu sắc cảm giác đó, khi sáng lập chương trình đào tạo tại Simon Center, tôi đã đưa ra một cam kết bất biến: KHÔNG BAO GIỜ BỎ RƠI HỌC VIÊN SAU KHÓA HỌC!

Khi bạn hoàn thành chương trình đào tạo, bạn không chỉ nhận được chứng chỉ. Bạn được kết nạp vào MẠNG LƯỚI CỰU HỌC VIÊN ALUMNI & HỘI ĐỒNG CHUYÊN MÔN DISC:

1. Hội đồng hội chẩn 24/7:
Bất cứ khi nào bạn tiếp nhận một ca bệnh khó tại cơ sở của mình, chỉ cần chụp ảnh phim X-quang và gửi thông tin bệnh sử vào nhóm chuyên môn kín. Các giảng viên và hội đồng bác sĩ DISC sẽ cùng bạn phân tích, đo góc lệch và định hướng phác đồ nắn chỉnh an toàn nhất. Bạn luôn có một "Hội đồng cố vấn y khoa quốc tế" đứng sau lưng bảo trợ!

2. Cập nhật kiến thức định kỳ:
Mỗi quý, Simon Center tổ chức các buổi Clinical Case Study Review để mổ xẻ các ca lâm sàng kinh điển, cập nhật các nghiên cứu mới nhất từ Đức và Mỹ hoàn toàn miễn phí.

3. Quyền lợi thực tập lâm sàng:
Học viên được phép đăng ký các ngày đi lâm sàng thực tế (Tageshospitation) tại phòng khám Simon Center để quan sát chuyên gia điều trị thực tế trên bệnh nhân thật.

Học một lần, nhưng sự đồng hành và bảo trợ chuyên môn là TRỌN ĐỜI.
👉 Đăng ký phỏng vấn tham gia khóa đào tạo mới tại đây: [ĐIỀN FORM TẠI ĐÂY]"""
            }
        ]
    },
    {
        "day": 6,
        "date": "19/09",
        "dayName": "Thứ Bảy",
        "theme": "Mở Cổng Chiêu Sinh Khóa Mới: Giới Hạn Suất Ưu Tiên & Quà Tặng Độc Quyền",
        "status": "Kế hoạch sẵn sàng",
        "posts": [
            {
                "time": "Sáng 08:00",
                "channel": "fanpage",
                "channelName": "Fanpage Học Viện",
                "voice": "voice3",
                "voiceName": "Giọng 3 (Chiêu sinh chính thức)",
                "title": "Chính thức mở cổng đăng ký: Khóa Đào Tạo Chiropractic Chuẩn Y Khoa Kế Thừa Nền Tảng DISC Academy",
                "cta": "Điền form giữ chỗ ưu tiên 5 suất sớm nhất nhận ưu đãi",
                "content": """[THÔNG BÁO CHÍNH THỨC: MỞ CỔNG CHIÊU SINH KHÓA ĐÀO TẠO CHIROPRACTIC CHUẨN Y KHOA — KHÓA MỚI]

Sau nhiều tháng hoàn thiện hệ thống học liệu và chuẩn bị cơ sở vật chất thực hành đạt tiêu chuẩn khắt khe của Đức, Simon Center xin trân trọng thông báo:

CHÍNH THỨC MỞ CỔNG TIẾP NHẬN ĐĂNG KÝ
CHƯƠNG TRÌNH ĐÀO TẠO CHIROPRACTIC CHUẨN Y KHOA (DISC ACADEMY STANDARD)

Vì nguyên tắc đào tạo cao nhất là CẦM TAY CHỈ VIỆC và ĐẢM BẢO 100% HỌC VIÊN RA NGHỀ PHẢI NẮN ĐƯỢC THẬT VÀ AN TOÀN TUYỆT ĐỐI, chúng tôi chỉ nhận tối đa 10 - 12 HỌC VIÊN cho mỗi khóa!

🎯 KHUNG CHƯƠNG TRÌNH TOÀN DIỆN 3 TẦNG:
- Tầng 1: Nền tảng E-Learning 4K chuyên sâu (Giải phẫu chức năng, Cơ sinh học Lovett Reactor, Giải mã phim X-quang Full-Spine và Bộ quy tắc Cảnh báo đỏ Red Flags).
- Tầng 2: Hệ thống Micro-Drills rèn phản xạ tại nhà (Bóc tách kỹ thuật, kiểm soát lực rơi Body Drop và các bài test tình huống lâm sàng qua môn bắt buộc).
- Tầng 3: Khóa huấn luyện Cầm tay chỉ việc trực tiếp 4-5 ngày cùng Giảng viên DISC (Chỉnh từng góc đặt tay, thực hành nắn chỉnh trên giường Drop Table chuẩn Hoa Kỳ).

🎁 ĐẶC QUYỀN DÀNH CHO 5 HỌC VIÊN ĐĂNG KÝ SỚM NHẤT:
1. Tặng trọn bộ tài khoản E-Learning 4K xem lại trọn đời trị giá 14.900.000đ.
2. Tặng bộ dụng cụ chuyên dụng rèn luyện lực rơi Micro-Drill tại nhà.
3. Miễn phí tư cách thành viên Mạng lưới cựu học viên Alumni hỗ trợ hội chẩn ca bệnh 24/7.
4. Ưu đãi trực tiếp 20% học phí cho đợt tuyển sinh đầu tiên.

👉 Cổng đăng ký sẽ tự động đóng lại khi đủ 12 học viên đạt yêu cầu phỏng vấn.
Điền thông tin giữ suất ưu tiên ngay tại đây: [ĐIỀN FORM ĐĂNG KÝ TẠI ĐÂY]"""
            },
            {
                "time": "Trưa 11:30",
                "channel": "tiktok_reels",
                "channelName": "TikTok / Reels",
                "voice": "voice2",
                "voiceName": "Giọng 2 (Tặng quà tri thức)",
                "title": "Tặng Cẩm nang độc quyền: 'Bản đồ định vị X-quang Cột sống & Quy trình kiểm soát 10 Cảnh báo đỏ' cho 20 người đầu tiên",
                "cta": "Tải miễn phí bản PDF chất lượng cao tại link bio",
                "content": """[VIDEO REELS/TIKTOK 60S: QUÀ TẶNG TÀI LIỆU CHUYÊN SÂU!]

[VISUAL]:
- Giảng viên cầm trên tay cuốn Cẩm nang in màu sắc nét với các hình ảnh phim X-quang, đường kẻ đo góc độ và bảng màu cảnh báo đỏ.
- Text: "Món quà vô giá cho những ai đang làm nghề trị liệu cột sống!"

[VOICE-OVER]:
Bạn làm nghề trị liệu cơ xương khớp nhưng chưa từng được ai hướng dẫn bài bản cách đọc phim X-quang?
Bạn luôn lo sợ những ca bệnh tai biến ngoài ý muốn?

Hôm nay, Simon Center xin gửi tặng cộng đồng cuốn cẩm nang lưu hành nội bộ cực kỳ tâm huyết:
"BẢN ĐỒ ĐỊNH VỊ X-QUANG CỘT SỐNG & QUY TRÌNH KIỂM SOÁT 10 CẢNH BÁO ĐỎ LÂM SÀNG"

Bên trong cuốn cẩm nang này có gì?
1. Hướng dẫn chi tiết cách kẻ 3 đường trục cơ bản trên phim X-quang cổ và thắt lưng để phát hiện trượt đốt sống trong 30 giây.
2. Bảng đối chiếu cặp đốt phản chiếu Lovett Reactor — tìm đúng đốt lệch tiên phát ở cổ khi bệnh nhân đau lưng.
3. Bảng checklist 10 Cảnh báo đỏ (Red Flags) — giúp bạn biết chính xác khi nào TUYỆT ĐỐI KHÔNG ĐƯỢC NẮN để bảo vệ an toàn cho bệnh nhân và cho chính bạn!

Tài liệu được chuyển ngữ và chuẩn hóa từ giáo trình DISC Academy Đức.
Bấm ngay vào link bio đầu trang, điền email để tải về bản PDF chất lượng cao hoàn toàn miễn phí nhé!"""
            },
            {
                "time": "Tối 20:00",
                "channel": "fb_personal",
                "channelName": "FB Cá Nhân",
                "voice": "voice3",
                "voiceName": "Giọng 3 (Lọc đối tượng - Tiêu chuẩn cao)",
                "title": "Những ai phù hợp (và ai TUYỆT ĐỐI KHÔNG NÊN đăng ký) khóa đào tạo Chiropractic tại Simon Center?",
                "cta": "Điền form để được bộ phận chuyên môn liên hệ phỏng vấn",
                "content": """Trước khi bạn quyết định điền form đăng ký khóa học Chiropractic tại Simon Center, tôi xin phép được nói rất rõ ràng và thẳng thắn điều này:

Khóa học này KHÔNG DÀNH CHO TẤT CẢ MỌI NGƯỜI.

❌ XIN VUI LÒNG ĐỪNG ĐĂNG KÝ NẾU BẠN THUỘC 3 NHÓM SAU:
1. Những người tìm kiếm một khóa học cấp tốc 1-2 ngày để lấy cái bằng đối phó và về nhà đè người khác ra bẻ răng rắc quay clip câu view TikTok. Chúng tôi không bao giờ tiếp tay cho lối làm nghề vô trách nhiệm đó.
2. Những người lười học lý thuyết giải phẫu, coi thường việc đọc phim X-quang và không chịu làm bài tập rèn lực Micro-drills tại nhà.
3. Những người đặt mục tiêu kiếm tiền nhanh chóng lên trên sự an toàn và y đức đối với người bệnh.

✅ CHÚNG TÔI CHỈ CHÀO ĐÓN NHỮNG HỌC VIÊN CÙNG HỆ GIÁ TRỊ:
- Các Bác sĩ YHCT, Kỹ thuật viên VLTL/PHCN muốn làm chủ kỹ thuật nắn chỉnh chuẩn y khoa quốc tế để nâng cao hiệu quả điều trị và gia tăng thu nhập xứng đáng.
- Các Huấn luyện viên PT, Yoga, Pilates muốn thấu hiểu căn nguyên sai lệch trục cơ thể để giải phóng cho học viên của mình một cách khoa học nhất.
- Những chủ cơ sở Spa, phòng khám trị liệu muốn xây dựng dịch vụ nắn chỉnh uy tín, chuẩn Đức, nói KHÔNG với tai biến.
- Và bất kỳ ai có niềm đam mê sâu sắc với cột sống con người, khao khát học nghề một cách chuẩn mực, bài bản và tử tế nhất!

Nếu bạn thấy mình thuộc nhóm thứ hai, chúng tôi rất vinh dự và sẵn sàng đồng hành cùng bạn trên hành trình trở thành một Master Chiropractic thực thụ.
👉 Điền form để chuyên môn phỏng vấn và giữ chỗ đợt này nhé ạ: [ĐIỀN FORM TẠI ĐÂY]"""
            }
        ]
    },
    {
        "day": 7,
        "date": "20/09",
        "dayName": "Chủ Nhật",
        "theme": "Chốt Danh Sách Đợt 1 & Lời Khuyên Chân Thành Cho Sự Nghiệp",
        "status": "Kế hoạch sẵn sàng",
        "posts": [
            {
                "time": "Sáng 08:00",
                "channel": "fanpage",
                "channelName": "Fanpage Học Viện",
                "voice": "voice3",
                "voiceName": "Giọng 3 (Chốt deal cấp thiết)",
                "title": "Chỉ còn 3 suất cuối đợt ưu tiên: Cơ hội nâng tầm từ người làm thuê thành Chuyên gia nắn chỉnh an toàn",
                "cta": "Điền form giữ 3 suất ưu tiên cuối cùng trước khi đóng cổng",
                "content": """[THÔNG BÁO: CHỈ CÒN ĐÚNG 3 SUẤT CUỐI CÙNG CHO KHÓA CHIÊU SINH ĐỢT 1!]

Sau 24 giờ mở cổng đăng ký chính thức, Simon Center vô cùng cảm kích trước sự đón nhận nồng nhiệt từ cộng đồng anh em Bác sĩ, Kỹ thuật viên VLTL, Huấn luyện viên PT trên khắp cả nước.

Tính đến 07:30 sáng nay:
Đã có 9/12 học viên hoàn tất thủ tục phỏng vấn chuyên môn và xác nhận tham gia khóa đào tạo.
Hiện tại, chúng tôi CHỈ CÒN ĐÚNG 3 SUẤT CUỐI CÙNG để nhận chính sách ưu đãi đặc quyền đợt 1!

Vì sao chúng tôi kiên quyết không nhận thêm dù nhu cầu đăng ký còn rất nhiều?
Bởi vì tôn chỉ của Simon Center là: ĐÀO TẠO THẬT — RA NGHỀ THẬT.
Trong các buổi thực hành trực tiếp, một giảng viên chỉ có thể kèm tối đa 5-6 học viên thì mới có thể cầm tay từng người, uốn nắn từng góc đặt ngón tay, chỉnh từng chuyển động rơi cơ thể (Body Drop) và sửa từng lỗi sai nhỏ nhất. Nhận đông học viên để tăng doanh thu là phản bội lại triết lý giáo dục chuẩn Đức!

Nếu bạn đã theo dõi Simon Center suốt những ngày qua, nếu bạn đang khao khát:
- Thoát khỏi cảnh xoa bóp mỏi mệt bắp tay, thu nhập bấp bênh.
- Tự tin đọc thấu phim X-quang, định vị chính xác đốt lệch tiên phát.
- Nắm chắc lằn ranh an toàn trọn đời, không bao giờ sợ tai biến.
- Sở hữu hội đồng chuyên gia DISC hỗ trợ hội chẩn ca bệnh 24/7.

Thì đây chính là thời điểm để bạn ra quyết định cho tương lai của mình!
Cổng đăng ký sẽ chính thức đóng lại khi 3 suất cuối cùng được lấp đầy.
👉 Giữ chỗ ưu tiên ngay bây giờ tại đây: [ĐIỀN FORM TẠI ĐÂY]"""
            },
            {
                "time": "Trưa 11:30",
                "channel": "group_community",
                "channelName": "Group Kỹ Thuật Viên Trị Liệu",
                "voice": "voice1",
                "voiceName": "Giọng 1 (Q&A Giải đáp)",
                "title": "Q&A Giải đáp trực tiếp: Học online liệu có nắn được trên người thật không? Bằng cấp chứng nhận ra sao?",
                "cta": "Để lại câu hỏi dưới phần bình luận để được giải đáp 1-1",
                "content": """Chào các anh chị em đồng nghiệp,

Trong 2 ngày mở cổng đăng ký vừa qua, bên cạnh những anh chị đã hoàn tất ghi danh, tôi nhận được khá nhiều câu hỏi băn khoăn rất chính đáng. Tôi xin được giải đáp công khai và minh bạch 3 thắc mắc lớn nhất để mọi người hoàn toàn yên tâm:

❓ Câu hỏi 1: "Nắn chỉnh là môn thực hành trực tiếp, học online liệu có làm được thật không thầy?"
Trả lời: Hoàn toàn làm được, nếu học đúng phương pháp! Chương trình online của Simon Center không phải là các video lý thuyết nói suông. Bạn được trang bị hệ thống bài tập phản xạ vi mô (Micro-drills) để tự rèn luyện góc đặt tay, hướng rơi cơ thể trên bóng và đệm chuyên dụng tại nhà. Sau mỗi bài đều có bài test tình huống bắt buộc vượt qua mới mở bài tiếp. Đây là bước chuẩn bị hoàn hảo nhất để khi bạn bước vào nắn trên người thật, tay nghề đã vững vàng và không còn cảm giác lúng túng!

❓ Câu hỏi 2: "Khóa học có thực hành trực tiếp cầm tay chỉ việc không?"
Trả lời: Chắc chắn có! Chương trình toàn diện của Simon Center kết hợp mô hình Hybrid: Sau khi bạn nắm chắc 100% lý thuyết và phản xạ Micro-drills trên hệ thống E-Learning, bạn sẽ tham gia các ngày huấn luyện thực hành Cầm tay chỉ việc trực tiếp cùng Giảng viên DISC tại phòng khám, được nắn chỉnh trên giường Drop Table và sửa lỗi trực tiếp 1-1.

❓ Câu hỏi 3: "Sau khi học xong tôi nhận được chứng chỉ gì?"
Trả lời: Bạn sẽ được cấp Chứng nhận hoàn thành chương trình Đào tạo Kỹ thuật Nắn chỉnh Chiropractic Chuẩn Y Khoa từ Simon Center (chứng nhận chuẩn hóa theo chương trình chuyển giao của DISC Academy Đức) — bảo chứng vững chắc nhất cho tay nghề và uy tín của bạn trước bệnh nhân.

Nếu bạn còn bất kỳ thắc mắc nào, hãy để lại bình luận hoặc nhắn tin trực tiếp để tôi giải đáp nhé ạ!
👉 Link đăng ký thông tin: [ĐIỀN FORM TẠI ĐÂY]"""
            },
            {
                "time": "Tối 20:30",
                "channel": "fb_personal",
                "channelName": "FB Cá Nhân",
                "voice": "voice3",
                "voiceName": "Giọng 3 (Triết lý nghề nghiệp & Tổng kết)",
                "title": "Đầu tư cho tay nghề và sự an toàn của người bệnh là khoản đầu tư sinh lời bền vững nhất trong sự nghiệp của bạn",
                "cta": "Cổng chiêu sinh đợt 1 khép lại, hẹn gặp lại các bạn tại lớp học",
                "content": """Đêm nay, một tuần đồng hành cùng chiến dịch truyền thông "Chuẩn Hóa Nghề Nắn Chỉnh Chiropractic Chuẩn Y Khoa" đã chính thức khép lại.

Tôi xin gửi lời cảm ơn chân thành và sâu sắc nhất đến toàn thể anh chị em đồng nghiệp, các Bác sĩ, Kỹ thuật viên, Huấn luyện viên thể hình trên cả nước đã theo dõi, tương tác và cùng tôi chia sẻ những trăn trở về nghề.

Xin chúc mừng 12 học viên xuất sắc đã chính thức hoàn tất thủ tục ghi danh và trở thành những thành viên mới của ngôi nhà chung Simon Center - DISC Academy!

Tôi luôn tin rằng: Trong cuộc đời mỗi con người, tiền bạc có thể đến rồi đi, cơ hội kinh doanh có thể thay đổi theo thời cuộc. Nhưng CÁI TÂM Y ĐỨC và TAY NGHỀ CHUẨN XÁC là thứ tài sản duy nhất không ai có thể lấy đi được của bạn.

Khi bạn nắm vững kiến thức đọc phim X-quang, khi bạn biết chính xác khi nào tuyệt đối không được nắn, khi bạn thực hiện cú nắn êm ái giải phóng cơn đau cho người bệnh mà trong lòng hoàn toàn tự tin, thanh thản và không chút sợ hãi — đó là lúc bạn không chỉ kiếm được tiền, mà bạn đang tích lũy phước lành và xây dựng một danh tiếng trường tồn.

Đầu tư cho tay nghề và sự an toàn của người bệnh là khoản đầu tư sinh lời bền vững nhất mà bạn từng thực hiện trong cuộc đời mình.

Cổng đăng ký đợt 1 chính thức khép lại.
Đội ngũ giảng viên Simon Center đang hoàn tất những khâu chuẩn bị giáo trình và thiết bị cuối cùng để chào đón các bạn vào tuần tới.

Hẹn gặp lại tất cả các bạn tại lớp học — nơi chúng ta cùng nhau đặt những viên gạch chuẩn mực đầu tiên cho ngành Chiropractic chuẩn y khoa tại Việt Nam!

Trân trọng và tự hào,
Founder Simon Center."""
            }
        ]
    }
]

# Random Topic Bank for Academy
random_topic_bank_academy = [
    { "title": "Tại sao 80% người học nắn chỉnh 2-3 ngày về nhà đều run tay không dám làm trên bệnh nhân thật?", "voice": "voice1", "channel": "fb_personal" },
    { "title": "Cú bẻ khớp 'răng rắc' trên TikTok vs Kỹ thuật nắn HVLA chuẩn Đức: Điểm khác biệt nguy hiểm", "voice": "voice2", "channel": "tiktok_reels" },
    { "title": "Đau thắt lưng nhưng đốt lệch tiên phát lại nằm ở cổ: Bài học xương máu từ DISC Academy Đức", "voice": "voice2", "channel": "fanpage" },
    { "title": "3 góc đo trượt đốt sống trên phim X-quang mà một Chiropractor chuyên nghiệp bắt buộc phải nắm trong 30 giây", "voice": "voice1", "channel": "fb_personal" },
    { "title": "Biết khi nào TUYỆT ĐỐI KHÔNG ĐƯỢC NẮN còn quan trọng gấp trăm lần học cách nắn!", "voice": "voice2", "channel": "fanpage" },
    { "title": "Nắn chỉnh không cần gồng cơ bắp tay: Bí mật công thức xung lực F·Δt = m·Δv giúp KTV nữ 45kg vẫn nắn êm ru", "voice": "voice2", "channel": "fb_personal" },
    { "title": "Bài toán hoàn vốn: Đầu tư khóa học Chiropractic chuẩn y khoa, chỉ cần 5-6 ca bệnh nhân là thu hồi toàn bộ học phí", "voice": "voice3", "channel": "fanpage" },
    { "title": "So sánh: Khóa học hội trường 2 ngày đông đúc vs Hệ sinh thái E-Learning 4K kèm cặp lâm sàng", "voice": "voice2", "channel": "tiktok_reels" },
    { "title": "Khách hỏi: 'Sao bên kia học phí nắn chỉnh chỉ vài triệu mà bên Simon Center học phí lại cao hơn?'", "voice": "voice3", "channel": "fb_personal" }
]

def update_file(file_path):
    print(f"Reading {file_path}...")
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    # 1. Replace plan7DaysData
    plan7_js = "const plan7DaysData = " + json.dumps(plan7_days_academy, ensure_ascii=False, indent=2) + ";"
    pattern_plan = r"const plan7DaysData\s*=\s*\[[\s\S]*?\n\s*\];"
    if re.search(pattern_plan, content):
        content = re.sub(pattern_plan, lambda m: plan7_js, content, count=1)
        print(" -> Replaced plan7DaysData successfully.")
    else:
        print(" -> Warning: plan7DaysData pattern not found!")

    # 2. Replace randomTopicBank
    bank_js = "const randomTopicBank = " + json.dumps(random_topic_bank_academy, ensure_ascii=False, indent=2) + ";"
    pattern_bank = r"const randomTopicBank\s*=\s*\[[\s\S]*?\n\s*\];"
    if re.search(pattern_bank, content):
        content = re.sub(pattern_bank, lambda m: bank_js, content, count=1)
        print(" -> Replaced randomTopicBank successfully.")
    else:
        print(" -> Warning: randomTopicBank pattern not found!")

    # 3. Update topicInput default value
    content = content.replace(
        'id="topicInput" value="Chúng ta đã học cách chịu đựng cơn đau giỏi đến mức nào?"',
        'id="topicInput" value="Tại sao 80% người học nắn chỉnh 2-3 ngày về nhà đều run tay không dám làm trên bệnh nhân thật?"'
    )
    content = content.replace(
        'Chủ đề: "Chúng ta đã học cách chịu đựng cơn đau giỏi đến mức nào?"',
        'Chủ đề: "Tại sao 80% người học nắn chỉnh 2-3 ngày về nhà đều run tay không dám làm trên bệnh nhân thật?"'
    )

    # 4. Update persona in buildGeminiSystemPrompt
    old_persona = 'let p = `Bạn là trợ lý mang tiếng nói của người sáng lập Simon Center (Chiropractic & PHCN tại TP.HCM).'
    new_persona = '''let p = `Bạn là trợ lý mang tiếng nói của Người Sáng Lập Simon Center & Giảng Viên Đào Tạo Chiropractic Chuẩn Y Khoa (kế thừa nền tảng lâm sàng Specific từ DISC Academy Đức).

SỨ MỆNH & ĐỊNH VỊ NỘI DUNG:
- Chuẩn hóa nghề nắn chỉnh tại Việt Nam, bài trừ nạn "bẻ khớp dạo 2 ngày" thô bạo gây nguy cơ tai biến y khoa.
- Đào tạo thế hệ Kỹ thuật viên VLTL/PHCN, Bác sĩ YHCT, HLV PT/Yoga/Pilates, Chủ cơ sở trị liệu trở thành Chuyên gia nắn chỉnh an toàn trọn đời thông qua:
  1. Đọc thấu phim X-quang Full-Spine để tìm đúng Đốt lệch tiên phát (Primary Subluxation) thay vì nắn mò theo chỗ đau.
  2. Nắm vững nguyên tắc khi nào TUYỆT ĐỐI KHÔNG ĐƯỢC NẮN (Quy trình tầm soát Cảnh báo đỏ - Red Flags) để bảo vệ bệnh nhân và uy tín cả đời.
  3. Phương pháp sư phạm Micro-Drills rèn phản xạ và lực rơi cơ thể (Body Drop) tại nhà trước khi chạm người thật.
- Kêu gọi hành động (CTA): Mời độc giả tải Cẩm nang đọc X-quang & Sàng lọc Red Flags, hoặc đăng ký nhận tư vấn Lộ trình Khóa Đào Tạo Chiropractic Chuẩn Y Khoa tại Simon Center.'''
    if old_persona in content:
        content = content.replace(old_persona, new_persona, 1)
        print(" -> Updated buildGeminiSystemPrompt persona.")

    # 5. Update CTA guideline in buildGeminiSystemPrompt
    old_cta_guide = "4. KÊU GỌI HÀNH ĐỘNG (CTA): Nhẹ nhàng mời điền Form Danh Sách Chờ (Waitlist) Buổi Đánh Giá Cột Sống 1-1 Chuyên Sâu để giữ chỗ ưu tiên (không giục giã, không ép mua hàng)."
    new_cta_guide = "4. KÊU GỌI HÀNH ĐỘNG (CTA): Hướng tới chiêu sinh học viên chuyên nghiệp: Mời đăng ký nhận Cẩm nang Đọc Phim X-quang Cột Sống & Checklist Red Flags, tham gia Workshop trực tuyến hoặc điền form Đăng Ký Tư Vấn Khóa Đào Tạo Chiropractic Chuẩn Y Khoa (số lượng giới hạn 10-12 người để cầm tay chỉ việc)."
    if old_cta_guide in content:
        content = content.replace(old_cta_guide, new_cta_guide, 1)
        print(" -> Updated CTA guideline in buildGeminiSystemPrompt.")

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Successfully saved {file_path}")

if __name__ == "__main__":
    update_file("/Users/huybui/Desktop/my-brain/index.html")

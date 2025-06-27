import logging
import os
from datetime import datetime

from src.exception import CustomException

LOG_FILE = f"{datetime.now().strftime('%Y-%m-%d')}.log"
logs_path = os.path.join(os.getcwd(), "logs", LOG_FILE)
os.makedirs(os.path.dirname(logs_path), exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler(logs_path),
        logging.StreamHandler()
    ]
)

# Bu bölüm, logger.py dosyasının doğrudan çalıştırılması durumunda örnek loglama işlemlerini gösterir.
# if __name__ == "__main__":
#
#     try:
#         # Sıfıra bölme hatası oluşturuluyor ve loglanıyor
#         a = 1 / 0  # Bu satır ZeroDivisionError hatası fırlatır
#     except Exception as e:
#         logging.error("Sıfıra bölme hatası oluştu.", exc_info=True)
#         raise CustomException(e) from e
#
#     # Loglama sisteminin kurulumunun tamamlandığına dair bilgi mesajı
#     logging.info("Loglama kurulumu tamamlandı.")
#     logging.debug("Bu bir debug mesajıdır.")
#     logging.warning("Bu bir uyarı mesajıdır.")
#     logging.error("Bu bir hata mesajıdır.")
#     logging.critical("Bu bir kritik mesajdır.")
#
#     # Fonksiyon içinde loglama örneği
#     def example_function():
#         logging.info("example_function fonksiyonundan bir info mesajı.")
#
#     example_function()  # Fonksiyonu çağırarak log mesajı oluşturulur
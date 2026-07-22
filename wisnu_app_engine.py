"""
=====================================================================
WISNU CYBER-CLOUD CONTROLLER v3.0
=====================================================================
Karya Mandiri / Tugas Besar Individu - Cloud Computing
Deskripsi: Sistem kendali otomatis siklus hidup S3 & EC2 LocalStack
=====================================================================
"""
import boto3
import sys
import time

class CyberCloudConsole:
    def __init__(self, endpoint="http://localhost:4566"):
        self.endpoint = endpoint
        print(" [SYSTEM] Menginisialisasi Wisnu Cyber-Cloud Core...")
        
        # Inisialisasi Kredensial Portabel
        try:
            self.s3 = boto3.client('s3', endpoint_url=endpoint, aws_access_key_id="wisnu", aws_secret_access_key="cyber", region_name="us-east-1")
            self.ec2 = boto3.client('ec2', endpoint_url=endpoint, aws_access_key_id="wisnu", aws_secret_access_key="cyber", region_name="us-east-1")
            print(f" [OK] Jalur transmisi terhubung ke endpoint: {endpoint}\n")
        except Exception as e:
            print(f" [ERROR] Kegagalan sistem transmisi: {e}")

    # ===============================================================
    # LAYANAN REKAYASA STORAGE (S3)
    # ===============================================================
    def s3_provisioning(self, bucket_name):
        print(f" ⚙️ [S3] Memulai instruksi pembuatan unit storage: '{bucket_name}'")
        try:
            self.s3.create_bucket(Bucket=bucket_name)
            print(f" 🟩 [SUCCESS] Storage '{bucket_name}' berhasil dipublikasikan di LocalStack.")
        except Exception as e:
            print(f" 🟥 [FAILED] Operasi S3 digagalkan server: {e}")

    def s3_deprovisioning(self, bucket_name):
        print(f" ⚙️ [S3] Memulai instruksi penghancuran unit storage: '{bucket_name}'")
        try:
            self.s3.delete_bucket(Bucket=bucket_name)
            print(f" 🟨 [TERMINATED] Storage '{bucket_name}' telah dihapus permanen.")
        except Exception as e:
            print(f" 🟥 [FAILED] Penghapusan gagal (Pastikan bucket kosong): {e}")

    # ===============================================================
    # LAYANAN REKAYASA COMPUTE (EC2)
    # ===============================================================
    def ec2_deployment(self, vm_type="t2.micro"):
        print(f" ⚙️ [EC2] Mengalokasikan virtual core untuk tipe instansi: {vm_type}")
        try:
            response = self.ec2.run_instances(
                ImageId='ami-cyberpunk99', 
                MinCount=1, MaxCount=1, 
                InstanceType=vm_type
            )
            instance_id = response['Instances'][0]['InstanceId']
            print(f" 🟩 [SUCCESS] Virtual Machine aktif dengan ID Unik: {instance_id}")
            return instance_id
        except Exception as e:
            print(f" 🟥 [FAILED] Deployment EC2 dihentikan: {e}")
            return None

    def ec2_termination(self, instance_id):
        if not instance_id:
            print(" 🟥 [ERROR] ID Instansi target tidak valid.")
            return
        print(f" ⚙️ [EC2] Memulai dekomposisi virtual machine ID: {instance_id}")
        try:
            self.ec2.terminate_instances(InstanceIds=[instance_id])
            print(f" 🟨 [TERMINATED] Virtual Machine {instance_id} sukses dihancurkan.")
        except Exception as e:
            print(f" 🟥 [FAILED] Perintah penghancuran ditolak: {e}")

# --- PENGUJIAN OTOMATIS RUNTIME ---
if __name__ == "__main__":
    print("====================================================")
    print("      🚀 WELCOME TO WISNU CYBER-CLOUD SYSTEM        ")
    print("====================================================\n")
    
    # Menjalankan konsol utama
    console = CyberCloudConsole()
    
    # Jalankan simulasi otomatis siklus hidup aset cloud
    target_storage = "cyber-storage-wisnu-tugas"
    console.s3_provisioning(target_storage)
    
    active_vm = console.ec2_deployment("t3.small")
    
    print("\n [INFO] Menahan status sistem untuk audit kelayakan tugas...")
    time.sleep(2)
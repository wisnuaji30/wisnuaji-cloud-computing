import boto3
import pandas as pd

# Konfigurasi Koneksi MiniStack / LocalStack Lokal
URL_ENDPOINT = "http://localhost:4566"

print("=== Luthfy Cloud Control — Sistem Aktif ===")

try:
    # Inisialisasi Kredensial AWS Dummy untuk Emulator
    s3 = boto3.client('s3', endpoint_url=URL_ENDPOINT, aws_access_key_id="mock", aws_secret_access_key="mock", region_name="us-east-1")
    ec2 = boto3.client('ec2', endpoint_url=URL_ENDPOINT, aws_access_key_id="mock", aws_secret_access_key="mock", region_name="us-east-1")
    
    # 1. FUNGSI UTAMA AMAZON S3 (CREATE & DELETE)
    def kelola_s3(nama_bucket, aksi="create"):
        if aksi == "create":
            s3.create_bucket(Bucket=nama_bucket)
            print(f"[✅ S3] Sukses Membuat Bucket: {nama_bucket}")
        elif aksi == "delete":
            s3.delete_bucket(Bucket=nama_bucket)
            print(f"[❌ S3] Sukses Menghapus Bucket: {name_bucket}")

    # 2. FUNGSI UTAMA AMAZON EC2 (CREATE & TERMINATE)
    def kelola_ec2(aksi="launch", instance_id=None):
        if aksi == "launch":
            res = ec2.run_instances(ImageId='ami-df5de724', MinCount=1, MaxCount=1, InstanceType='t2.micro')
            vmid = res['Instances'][0]['InstanceId']
            print(f"[✅ EC2] Sukses Menjalankan VM Baru dengan ID: {vmid}")
            return vmid
        elif aksi == "terminate" and instance_id:
            ec2.terminate_instances(InstanceIds=[instance_id])
            print(f"[❌ EC2] Perintah Hapus Dikirim untuk ID: {instance_id}")

    # --- Simulasi Otomatis Siklus Hidup Resource ---
    print("\n[*] Menjalankan pengujian sistem...")
    kelola_s3("bucket-tugas-luthfy", "create")
    id_baru = kelola_ec2("launch")
    
except Exception as e:
    print(f"\n[⚠️] Status Koneksi: Menunggu server LocalStack aktif di port 4566.")
    print(f"[!] Detail Log: {e}")
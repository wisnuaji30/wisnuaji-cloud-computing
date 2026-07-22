import boto3
import pandas as pd

# Alamat localhost komputer Anda
URL_LOCAL = "http://127.0.0.1:4566"

print("[*] Mencoba menyambungkan ke Localhost komputer Anda...")

try:
    # Koneksi otomatis ke MiniStack laptop Anda
    s3 = boto3.client('s3', endpoint_url=URL_LOCAL, aws_access_key_id="mock", aws_secret_access_key="mock", region_name="us-east-1")
    ec2 = boto3.client('ec2', endpoint_url=URL_LOCAL, aws_access_key_id="mock", aws_secret_access_key="mock", region_name="us-east-1")
    
    # 1. Tes membuat Bucket S3
    nama_bucket = "bucket-tugas-luthfy"
    s3.create_bucket(Bucket=nama_bucket)
    print(f"✅ SUKSES: Berhasil membuat S3 Bucket bernama '{nama_bucket}' di localhost!")
    
    # 2. Tes melihat daftar S3
    respon = s3.list_buckets()
    daftar = [b['Name'] for b in respon.get('Buckets', [])]
    print(f"📦 Daftar Bucket Aktif: {daftar}")
    
    # 3. Tes menjalankan EC2
    vm = ec2.run_instances(ImageId='ami-123456', MinCount=1, MaxCount=1, InstanceType='t2.micro')
    id_vm = vm['Instances'][0]['InstanceId']
    print(f"✅ SUKSES: Berhasil meluncurkan EC2 dengan ID '{id_vm}' di localhost!")

except Exception as e:
    print(f"❌ KONEKSI GAGAL: Pastikan aplikasi emulator MiniStack/LocalStack di laptop Anda sudah dinyalakan! \nDetail Error: {e}")
    
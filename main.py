#!/usr/bin/env python3
"""Entry untuk bounty make.fun "Sum up 20 November's world news in one image".

Program ini sengaja dibuat sesederhana mungkin: gambar finalnya, entry.png,
sudah jadi dan tersimpan di repositori ini di samping berkas ini. Tugas
program hanya menyalinnya ke /output/entry.png (atau ke $MAKEFUN_OUTPUT_DIR
di luar kontainer grader), persis seperti adanya — tanpa pemrosesan, tanpa
jaringan, tanpa jam dinding — sehingga dua kali jalan selalu menghasilkan
byte yang sama.

Gambarnya sendiri adalah satu halaman depan koran bergaya ilustrasi
editorial yang merangkum berita dunia Jumat 20 November 2026: KTT tiga
pemimpin di Shenzhen, putusan genosida ICJ terhadap Myanmar, aksi jual AI
di pasar global, rudal Houthi di Riyadh, dan berakhirnya wabah Ebola di
Kenya, dengan strip ticker berita lainnya di bagian bawah.
"""

import os
import shutil
from pathlib import Path

SUMBER = Path(__file__).resolve().parent / "entry.png"


def main() -> None:
    tujuan_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    tujuan_dir.mkdir(parents=True, exist_ok=True)
    tujuan = tujuan_dir / "entry.png"
    shutil.copyfile(SUMBER, tujuan)
    # Pastikan salinannya utuh: ukuran byte tujuan harus sama dengan sumbernya.
    if tujuan.stat().st_size != SUMBER.stat().st_size:
        raise SystemExit("salinan entry.png tidak utuh")
    print(f"entry.png tersalin ke {tujuan} ({tujuan.stat().st_size} byte)")


if __name__ == "__main__":
    main()

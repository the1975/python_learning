{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/the1975/python_learning/blob/main/Data_Processing_Tugas1.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "# Task Basic Python\n",
        "\n",
        "### Nama : Leonardo yanuarianto\n",
        "### NIM : 2513020074"
      ],
      "metadata": {
        "id": "qPfMD6i_pCdJ"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "## Input Output\n",
        "\n",
        "1. Cobalah buat Program Python Untuk menampilkan Biodata Anda dengan tampilan sebagai berikut\n",
        "\n",
        "```bash\n",
        "+------------------------+\n",
        "| Nama | Gender | Alamat |\n",
        "+------------------------+\n",
        "| Budi | L      | Kediri |\n",
        "+------------------------+\n",
        "| Susi | P      | Malang |\n",
        "+------------------------+\n",
        "| Rani | P      | Yogya  |\n",
        "+------------------------+\n",
        "| Dodi | L      | Nganjuk|\n",
        "+------------------------+\n",
        "```\n"
      ],
      "metadata": {
        "id": "fRFUoqVwpQJP"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "## Tulis Kode Disini\n",
        "print(\"+---------------------------+\") #29 char\n",
        "print(\"| {:<5} | {:<6} | {:<8} |\".format(\"Nama\",\"Gender\",\"Alamat\")) #.format agar tabel tetap sejajar\n",
        "print(\"+---------------------------+\")\n",
        "print(\"| {:<5} | {:<6} | {:<8} |\".format(\"Leo\",\"L\",\"Nganjuk\"))\n",
        "print(\"+---------------------------+\")"
      ],
      "metadata": {
        "id": "VO7iYzeypKcI",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "05fe1a06-3a3d-49b7-ada2-8a49088f224a"
      },
      "execution_count": 1,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "+---------------------------+\n",
            "| Nama  | Gender | Alamat   |\n",
            "+---------------------------+\n",
            "| Leo   | L      | Nganjuk  |\n",
            "+---------------------------+\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "2. Buatlah program untuk Kartu Ucapan Selamat Hari raya dimana nama akan di inputkan sendiri oleh user\n",
        "berikut adalah contoh tampilannya\n",
        "\n",
        "```bash\n",
        "Masukan Nama Anda : _Rudy Eko Prasetya_\n",
        "+-------------------------------------+\n",
        "| Selamat Hari raya                   |\n",
        "| Kepada Rudy Eko Prasetya            |\n",
        "| Mohon Maaf Lahir dan Batin          |\n",
        "+-------------------------------------+\n",
        "```"
      ],
      "metadata": {
        "id": "nM8nMTkevKaU"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "## Tulis Kode Disini\n",
        "name = input(\"Masukkan Nama Anda : \") #31 char\n",
        "print(\"+------------------------------+\")\n",
        "print(\"| Selamat Hari Raya            |\")\n",
        "print(\"| Kepada {:<22}|\".format(name)) #.format agar tabel tetap sejajar\n",
        "print(\"| Mohon Maaf Lahir Batin       |\")\n",
        "print(\"+------------------------------+\")"
      ],
      "metadata": {
        "id": "mQ8_IUaSvYzC",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "d65794c7-545d-42d6-e345-c355aaf3d367"
      },
      "execution_count": 2,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Masukkan Nama Anda : Leonardo yanuarianto\n",
            "+------------------------------+\n",
            "| Selamat Hari Raya            |\n",
            "| Kepada Leonardo yanuarianto  |\n",
            "| Mohon Maaf Lahir Batin       |\n",
            "+------------------------------+\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "## Variable dan Operator"
      ],
      "metadata": {
        "id": "nbUxuKdMvYAr"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "1. Pada Code dibawah ini carilah type data untuk variable a, b dan nama\n",
        "```bash\n",
        "a = 20\n",
        "b = 10\n",
        "nama = \"Rudy\"\n",
        "print('Nilai a =',a)\n",
        "print('Nilai b =',b)\n",
        "print('Nilai nama =',nama)\n",
        "```\n",
        "\n"
      ],
      "metadata": {
        "id": "-YFL-UwAvztc"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "## Tulis Kode Disini\n",
        "a = 20 # type int\n",
        "b = 10\n",
        "name = \"Leo\" # type str\n",
        "print('Nilai a =',a)\n",
        "print('Nilai b =',b)\n",
        "print('Nilai nama =',name)"
      ],
      "metadata": {
        "id": "GZcx2VGjwUz4",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "667e22e5-7603-494e-b837-e77d10488151"
      },
      "execution_count": 3,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Nilai a = 20\n",
            "Nilai b = 10\n",
            "Nilai nama = Leo\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "2. dari variable dibawah ini tuliskan hasil dari\n",
        "```bash\n",
        "a = 20\n",
        "b = 10\n",
        "\n",
        "a + b =\n",
        "a - b =\n",
        "a x b =\n",
        "a : b =\n",
        "a modulo b =\n",
        "```"
      ],
      "metadata": {
        "id": "QqJWfT77wYOp"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "a = 20\n",
        "b = 10\n",
        "\n",
        "print(a + b)\n",
        "print(a - b)\n",
        "print(a * b)\n",
        "print(a / b)\n",
        "print(a % b)\n"
      ],
      "metadata": {
        "id": "yXMABzw9xGyZ",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "cd3c057f-aa1b-4c41-d59f-ce2f0cc9ef62"
      },
      "execution_count": 4,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "30\n",
            "10\n",
            "200\n",
            "2.0\n",
            "0\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "3. dari nilai variable dibawah tentukan hasil dari\n",
        "\n",
        "```bash\n",
        "a = 10\n",
        "\n",
        "a += 5\n",
        "a -= 5\n",
        "a *= 5\n",
        "a /= 5\n",
        "```"
      ],
      "metadata": {
        "id": "HeWtHOmSxGFD"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "## Tulis Kode Disini\n",
        "\n",
        "a = 10\n",
        "\n",
        "a += 5\n",
        "print(a)\n",
        "\n",
        "a -= 5\n",
        "print(a)\n",
        "\n",
        "a *= 5\n",
        "print(a)\n",
        "\n",
        "a /= 5\n",
        "print(a)"
      ],
      "metadata": {
        "id": "hYvGwMpzxlQ7",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "ae68574f-6880-4fea-92f5-4a9fd02684e0"
      },
      "execution_count": 5,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "15\n",
            "10\n",
            "50\n",
            "10.0\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "4. dengan operator pembanding cari hasil dari\n",
        "\n",
        "```bash\n",
        "a = 20\n",
        "b = 10\n",
        "\n",
        "a sama dengan b hasilnya\n",
        "a tidak sama dengan b hasilnya\n",
        "a lebih dari b hasilnya\n",
        "a kurang dari b hasilnya\n",
        "a lebih dari sama dengan b hasilnya\n",
        "a kurang dari sama dengan b hasilnya\n",
        "```"
      ],
      "metadata": {
        "id": "nOi-BsfAx3UC"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "## Tulis Kode Disini\n",
        "a = 20\n",
        "b = 10\n",
        "\n",
        "print(a == b)\n",
        "print(a != b)\n",
        "print(a > b)\n",
        "print(a < b)\n",
        "print(a >= b)\n",
        "print(a <= b)"
      ],
      "metadata": {
        "id": "zpByG-D0yHVi",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "8e22ea02-87f5-4133-c531-39b726082637"
      },
      "execution_count": 6,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "False\n",
            "True\n",
            "True\n",
            "False\n",
            "True\n",
            "False\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "5. dengan menggunakan operator logika cari hasil dari\n",
        "\n",
        "```bash\n",
        "a = 0\n",
        "b = 1\n",
        "\n",
        "a AND b hasilnya\n",
        "a OR b hasilnya\n",
        "NOT b hasilnya\n",
        "```"
      ],
      "metadata": {
        "id": "JTkiIun8yORR"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "## Tulis Kode Disini\n",
        "a = 0\n",
        "b = 1\n",
        "\n",
        "print(a and b)\n",
        "print(a or b)\n",
        "print(not b)\n"
      ],
      "metadata": {
        "id": "GNIKYLsyyngD",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "61e598cb-e4dd-4693-c8ff-2250167eadc0"
      },
      "execution_count": 7,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "0\n",
            "1\n",
            "False\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "## EXAM 1\n",
        "\n",
        "1. Buatlah program pyhton dimana bisa perhitungan otomatis dengan python untuk mencari\n",
        "\n",
        "*   Volume Tabung\n",
        "*   Volume balok\n",
        "*   Luas Kerucut\n",
        "\n",
        "dimana nilai nilai input berasal dari user, berikut contohnya\n",
        "\n",
        "```bash\n",
        "Masukan Panjangnya(cm) = _2_\n",
        "Masukan Lebarnya(cm) = _3_\n",
        "Masukan Tingginya(cm) = _1_\n",
        "Maka Volume balok tersebut adalah 6\n",
        "```"
      ],
      "metadata": {
        "id": "-pwGQmr-yxFh"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "## Tulis Kode Disini\n",
        "\n",
        "p = float(input(\"Masukan Panjangnya(cm) = \"))\n",
        "l = float(input(\"Masukan Lebarnya(cm) = \"))\n",
        "t = float(input(\"Masukan Tingginya(cm) = \"))\n",
        "r = float(input('Masukan Jari-jarinya(cm) ='))\n",
        "s = float(input('Masukan garis pelukis(cm) ='))\n",
        "pi = 3.14\n",
        "\n",
        "volume_balok = p * l * t\n",
        "volume_tabung = pi * r * r * t\n",
        "luas_kerucut = pi * r * (r + s)\n",
        "\n",
        "output = f'''\n",
        "Maka Volume balok tersebut adalah, {volume_balok} cm\n",
        "Maka Volume tabung tersebut adalah, {volume_tabung} cm\n",
        "Maka Luas kerucut tersebut adalah, {luas_kerucut} cm\n",
        "'''\n",
        "\n",
        "print(output)"
      ],
      "metadata": {
        "id": "or7_L7hIzP7r",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "46e4f827-81e0-4207-c6ce-c1e2ef677577"
      },
      "execution_count": 19,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Masukan Panjangnya(cm) = 5\n",
            "Masukan Lebarnya(cm) = 8\n",
            "Masukan Tingginya(cm) = 9\n",
            "Masukan Jari-jarinya(cm) =9\n",
            "Masukan garis pelukis(cm) =3\n",
            "\n",
            "Maka Volume balok tersebut adalah, 360.0 cm\n",
            "Maka Volume tabung tersebut adalah, 2289.06 cm\n",
            "Maka Luas kerucut tersebut adalah, 339.12 cm\n",
            "\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "2. Buatlah program python untuk menentukan kelulusan suatu siswa dengan memasukan nilainya, dengan ketentuan lulus adalah lebih dari 70, berikut adalah contoh tampilannya\n",
        "\n",
        "```bash\n",
        "Masukan nama Anda = _Rudy_\n",
        "Masukan nilai Anda = _78_\n",
        "\n",
        "Selamat Rudy Nilai anda masuk dalam kriteria LULUS\n",
        "```"
      ],
      "metadata": {
        "id": "yPP1VheRzR5R"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "## Tulis Kode Disini\n",
        "nama = input(\"Masukan nama Anda = \")\n",
        "nilai = int(input(\"Masukan nilai Anda = \"))\n",
        "\n",
        "if nilai > 70:\n",
        "  print(f\"Selamat{nama}Nilai anda masuk dalam kriteria LULUS\")"
      ],
      "metadata": {
        "id": "YPT9K87vzj4l",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "1ba6a491-586e-4a02-e826-d962896b97d9"
      },
      "execution_count": 9,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Masukan nama Anda = leo\n",
            "Masukan nilai Anda = 90\n",
            "SelamatleoNilai anda masuk dalam kriteria LULUS\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "## Percabangan"
      ],
      "metadata": {
        "id": "sKRNpGkA3fR2"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "1. Buatlah program dimana Jika nilai diatas 75 maka dinyatakan Lulus Selain itu Remidi"
      ],
      "metadata": {
        "id": "FFEDjdau3idV"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "## Tulis Kode Disini\n",
        "nilai = int(input(\"Masukkan nilai anda = \"))\n",
        "if nilai > 75:\n",
        "  print (\"Selamat anda dinyatakan LULUS\")\n",
        "else:\n",
        "  print (\"nilai tidak mencukupi silahkan mengikuti REMIDI\")"
      ],
      "metadata": {
        "id": "SFdtdfab4BX9",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "b57b2316-af45-47a4-ce27-2f659eb62070"
      },
      "execution_count": 10,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Masukkan nilai anda = 90\n",
            "Selamat anda dinyatakan LULUS\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "2. Buatlah program unutk menentukan predikat nilai dimana\n",
        "*   nilai lebih dari 85 predikat A\n",
        "*   nilai lebih dari 75 predikat B\n",
        "*   nilai kurang dari 75 predikat C\n",
        "\n",
        "\n"
      ],
      "metadata": {
        "id": "s7tyEbth4KQE"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "## Tulis Kode Disini\n",
        "nilai = int(input(\"Masukkan nilai anda = \"))\n",
        "if nilai > 85:\n",
        "  print(\"anda mendapat Predikat A\")\n",
        "elif nilai > 75:\n",
        "  print (\"anda mendapat Predikat B\")\n",
        "else:\n",
        "  print(\"anda mendapat Predikat C\")"
      ],
      "metadata": {
        "id": "8cy8yp4Y4gW0",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "c8a3f072-ea80-4f0e-a5fb-1e54a314da44"
      },
      "execution_count": 11,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Masukkan nilai anda = 99\n",
            "anda mendapat Predikat A\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "## EXAM 2\n",
        "\n",
        "1. Buatlah program untuk menentukan nama nama hari berdasarkan angka yang di inputkan oleh user, contoh\n",
        "\n",
        "```bash\n",
        "PROGRAM NAMA HARI\n",
        "Pilihan\n",
        "1 = Senin\n",
        "2 = Selasa\n",
        "3 = Rabu\n",
        "4 = Kamis\n",
        "5 = Jumat\n",
        "6 = Sabtu\n",
        "7 = Minggu\n",
        "Masukan pilihan [1 s/d 7] = __\n",
        "```"
      ],
      "metadata": {
        "id": "qtVyHdFH4wDM"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "## Tulis Kode Disini\n",
        "print(\"\"\"PROGRAM NAMA HARI\n",
        "Pilihan\n",
        "1 = Senin\n",
        "2 = Selasa\n",
        "3 = Rabu\n",
        "4 = Kamis\n",
        "5 = Jumat\n",
        "6 = Sabtu\n",
        "7 = Minggu\"\"\")\n",
        "pilihan = int(input(\"Masukan pilihan [1 s/d 7] = \"))\n",
        "if pilihan == 1:\n",
        "  print (\"Hari: Senin\")\n",
        "elif pilihan == 2:\n",
        "  print (\"Hari: Selasa\")\n",
        "elif pilihan == 3:\n",
        "  print (\"Hari: Rabu\")\n",
        "elif pilihan == 4:\n",
        "  print(\"Hari: Kamis\")\n",
        "elif pilihan == 5:\n",
        "  print(\"Hari: Jumat\")\n",
        "elif pilihan == 6:\n",
        "  print (\"Hari: Sabtu\")\n",
        "elif pilihan == 7:\n",
        "  print (\"Hari Minggu\")"
      ],
      "metadata": {
        "id": "3iYnr4JD40K0",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "73186550-edc7-4751-e5de-d57386d1fcc7"
      },
      "execution_count": 12,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "PROGRAM NAMA HARI\n",
            "Pilihan\n",
            "1 = Senin\n",
            "2 = Selasa\n",
            "3 = Rabu\n",
            "4 = Kamis\n",
            "5 = Jumat\n",
            "6 = Sabtu\n",
            "7 = Minggu\n",
            "Masukan pilihan [1 s/d 7] = 7\n",
            "Hari Minggu\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "2. Buatlah program untuk mencari diskon dari suatu pembelian barang dengan kondisi\n",
        "*   Jika Pembelian diatas 100.000 dapat diskon 10%\n",
        "*   Jika Pembelian diatas 50.000 diskon 5%\n",
        "*   Selain itu tidak dapat diskon\n",
        "\n",
        "contoh\n",
        "\n",
        "```bash\n",
        "Masukan Total Pembelian = _200000_\n",
        "Diskon Anda = 20000\n",
        "Total Bayar Anda = 180000\n",
        "```"
      ],
      "metadata": {
        "id": "hLQlj3Dx48UN"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "## Tulis Kode Disini\n",
        "beli = float(input(\"Masukkan Total Pembelian = \"))\n",
        "if beli > 100.000:\n",
        "  diskon = beli * 0.10\n",
        "elif beli > 50.000:\n",
        "  diskon = beli * 0.05\n",
        "else:\n",
        "  diskon = 0\n",
        "total = beli - diskon\n",
        "print (\"Diskon anda =\", diskon)\n",
        "print (\"Total Bayar Anda\", total)"
      ],
      "metadata": {
        "id": "bp68DCyX5KT8",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "8b5c0275-3586-4d45-d959-37df70bd60b5"
      },
      "execution_count": 13,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Masukkan Total Pembelian = 7000\n",
            "Diskon anda = 700.0\n",
            "Total Bayar Anda 6300.0\n"
          ]
        }
      ]
    }
  ]
}
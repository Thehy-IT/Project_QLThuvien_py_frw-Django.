# Generated by Django 5.0.14 on 2025-06-18 07:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Book",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "book_id",
                    models.CharField(
                        max_length=20, unique=True, verbose_name="ID Sách"
                    ),
                ),
                ("title", models.CharField(max_length=255, verbose_name="Tên Sách")),
                ("author", models.CharField(max_length=255, verbose_name="Tác Giả")),
                ("pages", models.IntegerField(verbose_name="Số Trang")),
                ("publication_year", models.IntegerField(verbose_name="Năm Xuất Bản")),
                (
                    "status",
                    models.IntegerField(
                        choices=[(0, "Có sẵn"), (1, "Đã mượn"), (2, "Trạng thái khác")],
                        default=0,
                        verbose_name="Trạng Thái Sách",
                    ),
                ),
                (
                    "category",
                    models.CharField(
                        choices=[
                            ("TIEU_THUYET", "Tiểu thuyết"),
                            ("GIAO_KHOA", "Giáo khoa"),
                            ("KHOA_HOC", "Khoa học"),
                        ],
                        max_length=50,
                        verbose_name="Chủng Loại Sách",
                    ),
                ),
            ],
            options={
                "verbose_name": "Sách",
                "verbose_name_plural": "Sách",
            },
        ),
        migrations.CreateModel(
            name="Member",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "member_id",
                    models.CharField(
                        max_length=20, unique=True, verbose_name="ID Thành Viên"
                    ),
                ),
                (
                    "name",
                    models.CharField(max_length=255, verbose_name="Tên Thành Viên"),
                ),
            ],
            options={
                "verbose_name": "Thành viên",
                "verbose_name_plural": "Thành viên",
            },
        ),
        migrations.CreateModel(
            name="BorrowRecord",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "borrow_date",
                    models.DateField(auto_now_add=True, verbose_name="Ngày Mượn"),
                ),
                (
                    "return_date",
                    models.DateField(blank=True, null=True, verbose_name="Ngày Trả"),
                ),
                ("due_date", models.DateField(verbose_name="Ngày Hết Hạn")),
                (
                    "book",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="library.book",
                        verbose_name="Sách",
                    ),
                ),
                (
                    "member",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="library.member",
                        verbose_name="Thành viên",
                    ),
                ),
            ],
            options={
                "verbose_name": "Bản ghi mượn",
                "verbose_name_plural": "Bản ghi mượn",
            },
        ),
    ]

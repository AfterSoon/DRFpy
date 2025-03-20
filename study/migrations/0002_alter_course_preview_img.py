from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("study", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="course",
            name="preview_img",
            field=models.ImageField(
                blank=True,
                help_text="Загрузите изображение для превью (необязательно).",
                null=True,
                upload_to="course_previews/",
                verbose_name="Превью курса",
            ),
        ),
    ]
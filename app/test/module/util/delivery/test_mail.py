from app.main.modules.util.delivery.mail import *


def test_send_mail_text():
    send_mail(
        send_from='yhlee@artience.com',
        send_to=['yhlee@artience.com'],
        subject='테스트메일',
        text='테스트메일 내용입니다.'
    )
    assert True


def test_send_mail_html():
    send_mail(
        send_from='yhlee@artience.com',
        send_to=['yhlee@artience.com'],
        subject='테스트메일',
        html='<html><h1>Title</h1><br/><b>Bold</b></html>'
    )
    assert True


def test_send_mail_file():
    send_mail(
        send_from='yhlee@artience.com',
        send_to=['yhlee@artience.com'],
        subject='테스트메일',
        text='테스트메일 내용입니다.',
        files=['./test_file.xlsx']
    )
    assert True



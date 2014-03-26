from account.forms import SignupForm
from simplemathcaptcha.fields import MathCaptchaField


class SignupFormWithCaptcha(SignupForm):
    captcha = MathCaptchaField()


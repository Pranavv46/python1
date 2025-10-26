#bool variable
has_account=True

#email variable
email_verified=False

can_login=has_account and email_verified

email='g@example.com'
is_email_valid="@" in email

user_age=17
is_age_valid= user_age >= 18
can_login_final=has_account and email_verified and is_email_valid and is_age_vald

print("Can login (account + verified):", can_login)
print("Is email valid:", is_email_valid)
print("Is age valid:", is_age_valid)
print("Final login allowed:", can_login_final)
#final
print("has account",has_account is True)
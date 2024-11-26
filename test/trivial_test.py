from social_age import get_social_status


def check_child():
    age = 8
    expect = 'ребенок'
    func_res = get_social_status(age)
    # if expect == func_res:
    #     print('work')
    # else:
    #     print('doesnt work')
    assert expect == func_res, 'not matched'


def check_adult():
    age = 33
    expect = 'взрослый'
    func_res = get_social_status(age)
    assert expect == func_res, 'not matched'


if __name__ == '__main__':
    check_child()
    check_adult()

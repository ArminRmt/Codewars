

#  With input "10.0.0.0", "10.0.0.50"  => return   50
#  With input "10.0.0.0", "10.0.1.0"   => return  256
#  With input "20.0.0.10", "20.0.1.0"  => return  246


# easy solution

from ast import Or


def ips_between(start, end):
    start_ip_array = start.split('.')
    end_ip_array = end.split('.')

    first_part = int(end_ip_array[3]) - int(start_ip_array[3])
    second_part = (int(end_ip_array[2]) - int(start_ip_array[2])) * 256
    third_part = (int(end_ip_array[1]) - int(start_ip_array[1])) * pow(256, 2)
    end_part = (int(end_ip_array[0]) - int(start_ip_array[0])) * pow(256, 3)

    return sum([first_part, second_part, third_part, end_part])


#  import ip_address

# from ipaddress import ip_address

def ips_between(start, end):
    return int(ip_address(end)) - int(ip_address(start))


# mathematical solution

def ips_between(start, end):
    a = sum([int(e)*256**(3-i) for i, e in enumerate(start.split('.'))])
    b = sum([int(e)*256**(3-i) for i, e in enumerate(end.split('.'))])
    return abs(a-b)


# Clever

def ips_between(start, end):
    return sum((int(b) - int(a)) * 256 ** i for i, (b, a) in enumerate(reversed(zip(end.split('.'), start.split('.')))))

# Or


def ips_between(start, end):
    n1 = int(''.join(f'{n:08b}' for n in map(int, start.split('.'))), 2)
    n2 = int(''.join(f'{n:08b}' for n in map(int, end.split('.'))), 2)
    return n2 - n1

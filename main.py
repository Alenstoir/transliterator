from dynaconf import settings
import re

from dll import Dll

LOREM = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum'

LOREM_ENG = 'But I must explain to you how all this mistaken idea of denouncing pleasure and praising pain was born and I will give you a complete account of the system, and expound the actual teachings of the great explorer of the truth, the master-builder of human happiness. No one rejects, dislikes, or avoids pleasure itself, because it is pleasure, but because those who do not know how to pursue pleasure rationally encounter consequences that are extremely painful. Nor again is there anyone who loves or pursues or desires to obtain pain of itself, because it is pain, but because occasionally circumstances occur in which toil and pain can procure him some great pleasure. To take a trivial example, which of us ever undertakes laborious physical exercise, except to obtain some advantage from it? But who has any right to find fault with a man who chooses to enjoy a pleasure that has no annoying consequences, or one who avoids a pain that produces no resultant pleasure?'


def is_gl(letter):
    if letter.lower() in settings.VOK_EN.GL:
        return True
    else:
        return False


def is_con(letter):
    if letter.lower() in settings.VOK_EN.CON:
        return True
    else:
        return False


def parse_gl(node):
    l_type = 1
    attempt = 1
    if node.next is not None:
        spinner = node.next
        if spinner.next is not None:
            while is_con(spinner.next.data) or spinner.next.data == 'e':
                attempt += 1
                spinner = spinner.next
                if spinner.next is not None:
                    pass
                else:
                    l_type = 2
                    break
        else:
            if is_con(spinner.data):
                l_type = 2

    if node.data.lower() == 'a':
        if l_type == 1:
            return 'ЭЙ'
        else:
            return 'Э'
    if node.data.lower() == 'e':
        if l_type == 1:
            return 'И'
        else:
            return 'Э'
    if node.data.lower() == 'i':
        if l_type == 1:
            return 'АЙ'
        else:
            return 'И'
    if node.data.lower() == 'o':
        if node.next is not None:
            if node.next.data == 'o':
                return 'У'
        if l_type == 1:
            return 'ОУ'
        else:
            return 'О'
    if node.data.lower() == 'u':
        if l_type == 1:
            return 'Ю'
        else:
            return 'А'


def parse_con(node):
    if node.data.lower() == 'b':
        return 'Б'

    if node.data.lower() == 'c':
        if node.next is not None:
            if node.next.data == 'e' or node.next.data == 'i':
                return 'С'
        else:
            return 'К'

    if node.data.lower() == 'd':
        return 'Д'

    if node.data.lower() == 'f':
        return 'Ф'

    if node.data.lower() == 'g':
        if node.next is not None:
            if node.next.data == 'e' or node.next.data == 'i' or node.next.data == 'y':
                return 'ДЖ'
        else:
            return 'Г'

    if node.data.lower() == 'h':
        if node.next is not None and node.prev is None:
            if is_gl(node.next.data):
                return 'Х'
        else:
            return None

    if node.data.lower() == 'j':
        return 'ДЖ'

    if node.data.lower() == 'k':
        if node.prev is None and node.next is not None:
            if node.next.data == 'n':
                return None
        return 'К'

    if node.data.lower() == 'l':
        return 'Л'

    if node.data.lower() == 'm':
        return 'М'

    if node.data.lower() == 'n':
        return 'Н'

    if node.data.lower() == 'p':
        return 'П'

    if node.data.lower() == 'q':
        if node.next is not None:
            if node.next.data == 'u':
                return 'КВ'
        return 'КЬЮ'

    if node.data.lower() == 'r':
        if node.prev is None:
            return 'Р'
        if node.next is not None:
            if is_gl(node.next.data):
                return 'Р'
            return None
        return None

    if node.data.lower() == 's':
        if node.prev is None:
            return 'С'
        if node.next is not None:
            if is_con(node.next.data):
                return 'С'
            if node.prev is not None:
                if node.prev.data is not None:
                    if is_gl(node.prev.data) and is_gl(node.next.data):
                        return 'З'
        if node.next is None:
            if is_con(node.prev.data):
                if settings.VOK_EN.CON[node.prev.data] == 'zv':
                    return 'З'
                else:
                    return 'С'
            else:
                return 'З'
        return 'Л'

    if node.data.lower() == 't':
        return 'Т'

    if node.data.lower() == 'v':
        return 'В'

    if node.data.lower() == 'w':
        return 'В'

    if node.data.lower() == 'x':
        return 'КС'

    if node.data.lower() == 'y':
        if node.prev is None:
            return 'Й'
        if node.next is None:
            if node.prev is not None:
                if is_con(node.prev.data):
                    if settings.VOK_EN.CON[node.prev.data] != 'gl':
                        return 'И'
        return 'АЙ'

    if node.data.lower() == 'z':
        return 'З'

def mid_word(node):
    if node.data.lower() == 'a':
        pass
    if node.data.lower() == 'e':
        pass
    if node.data.lower() == 'i':
        pass
    if node.data.lower() == 'o':
        pass
    if node.data.lower() == 'u':
        pass


def end_word(node):
    if node.data.lower() == 'a':
        pass
    if node.data.lower() == 'e':
        pass
    if node.data.lower() == 'i':
        pass
    if node.data.lower() == 'o':
        pass
    if node.data.lower() == 'u':
        pass


def is_word(node):
    if node.data.lower() == 'a':
        pass
    if node.data.lower() == 'e':
        pass
    if node.data.lower() == 'i':
        pass
    if node.data.lower() == 'o':
        pass
    if node.data.lower() == 'u':
        pass


def count_gl(string):
    counter = 0
    for letter in string:
        if is_gl(letter):
            counter += 1
    return counter


def transliterate(dlls):
    text = []
    for dll in dlls:
        for letter in dll:
            if is_gl(letter.data):
                text.append(parse_gl(letter))
            else:
                text.append(parse_con(letter))
    print(text)


def syllablate(string):
    syl = ''
    syls = {}
    string = re.split(r'[;,\s]+', string)
    dlls = []
    print(string)
    for item in string:
        syls[item] = []
        iterator = len(item)
        dll = Dll()
        for letter in item[::]:
            dll.add(letter)
            if len(syl) > 2:
                if syl == 'ing':
                    syls[item].append(syl)
                    syl = letter
                else:
                    if is_con(syl[-1]):
                        if count_gl(syl) > 0:
                            if is_con(letter):
                                syl = syl + letter
                            else:
                                syls[item].append(syl[:-1])
                                syl = syl[-1] + letter
                        else:
                            syl = syl + letter
                    else:
                        if is_con(letter):
                            syls[item].append(syl)
                            syl = letter
                        else:
                            if letter in settings.VOK_EN.GL.i:
                                syls[item].append(syl)
                                syl = letter
                            else:
                                syl = syl + letter

            elif len(syl) == 2:
                if is_con(syl[-1]):
                    if count_gl(syl) > 0:
                        if is_gl(letter):
                            syls[item].append(syl[0])
                            syl = syl[1:] + letter
                        else:
                            syl = syl + letter
                    else:
                        syl = syl + letter
                else:
                    # print(syl, letter)
                    if is_gl(letter):
                        if letter in settings.VOK_EN.GL.i:
                            syls[item].append(syl)
                            syl = letter
                        else:
                            syl = syl + letter
                    else:
                        syl = syl + letter

            elif len(syl) == 1:
                if is_gl(syl):
                    if is_gl(letter):
                        syls[item].append(syl)
                        syl = letter
                    else:
                        syl = syl + letter
                else:
                    syl = syl + letter
            else:
                syl = letter

            iterator -= 1
            if iterator == 0:
                syls[item].append(syl)
                syl = ''
        dlls.append(dll)
    print(syls)

    transliterate(dlls)


if __name__ == '__main__':
    syllablate(LOREM_ENG)

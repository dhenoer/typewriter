import time
import random
import datetime as dt

class Typewriter:

    default_mode = 'ltr'

    @staticmethod
    def set_mode(mode):
        func_mode = {
            'ltr':__class__.print_ltr,
            'rtl':__class__.print_rtl,
            'scatter':__class__.print_scatter,
            }
        if mode in func_mode.keys():
           __class__.default_mode = mode
           __class__.default_func = func_mode[mode]
        else:
            print('-- Error: unkonwn mode --')

    @staticmethod
    def print_scatter(txt):
        len_txt = len(txt)
        pos = list(range(0, len_txt))
        random.shuffle(pos)
        dtxt = {}
        for i in range(len_txt): dtxt[i] = ' '

        print(' '*len_txt, end='')
        for p in pos:
            dtxt[p] = txt[p]
            print(chr(8)*len_txt ,end='')
            print(''.join(dtxt.values()), end='', flush=True)
            time.sleep(0.05)

    @staticmethod
    def print_rtl(txt):
        len_txt = len(txt)
        print(' '*len_txt, end='')
        for i in range(len_txt-1, -1, -1):
            print(chr(8)*len_txt ,end='')
            print(f'{txt[i:]:>{len_txt}}', end='', flush=True)
            time.sleep(0.1)

    @staticmethod
    def print_ltr(txt):
        for c in txt:
            print(c, end='', flush=True)
            time.sleep(0.1)

    @staticmethod
    def print(*arg, **kwarg):
        sep = kwarg.get('sep', ' ')
        mode = kwarg.get('mode', __class__.default_mode)
        __class__.set_mode(mode)

        t = [str(w) for w in arg ]
        txt = sep.join(t)
        __class__.default_func(txt)
        #__class__.func_mode[__class__.default_mode](txt)
        kwarg.pop('mode',None)
        print(**kwarg)

    @staticmethod
    def input(prompt, **kwarg):
        __class__.print(prompt, **kwarg, end='')
        return input()



if __name__ == '__main__':
    tw = Typewriter

    tw.print('Hari Ulang Tahun')
    tw.print('================', mode='rtl')
    tw.print()

    while True:
        nama = tw.input('Nama: ', mode='ltr')
        lahir = tw.input('Tanggal Lahir (tgl/bln/thn): ')
        tgl, bln, thn = map(int, lahir.split('/'))
        # inputan tgl/bln/thn perlu validasi

        hariLahir = dt.date(thn, bln, tgl)
        hariIni = dt.date.today()
        hariUltah = dt.date(hariIni.year, bln, tgl)

        dLahir = hariIni - hariLahir
        dUltah = hariUltah - hariLahir
        umur = hariIni.year - hariLahir.year
        lewatHari = dLahir - dUltah

        tw.print(f'Apa kabar {nama}?', mode='scatter')
        tw.print(f'Ulang tahun kamu yang ke {umur}', end=' ')
        if dLahir > dUltah:
            tw.print(f'sudah lewat {lewatHari.days} hari. Selamat ya..')
        else:
            tw.print(f'masih {abs(lewatHari.days)} hari lagi..')

        print()
        q = tw.input('Tekan [Enter] untuk lagi', mode='rtl')
        if q != '':
            break

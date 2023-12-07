from typing import Union
from pathlib import Path


def strftimestamp(timestamp: int):
    """
    Convert timestamp (seconds) to string %Y-%m-%d %H:%M:%S
    """
    from datetime import datetime

    return datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')


def strptimestamp(datetimestr: str):
    """
    Convert datetime string %Y-%m-%d %H:%M:%S to timestamp (seconds.)
    e.g. 1997-07-01 08:00:00 -> 867715200
    supports date (1997-01-01) or (1997/01/01)
    """
    from datetime import datetime

    for fmt in '%Y-%m-%d %H:%M:%S', '%Y-%m-%d':
        try:
            return datetime.strptime(datetimestr, fmt).timestamp()
        except ValueError:
            continue

    return datetime.strptime(datetimestr, '%Y/%m/%d').timestamp()


def get_title_number(path: Union[str, Path]):
    """
    Find the number in video title.
    e.g. "「BanG Dream! It's MyGO!!!!!」#1.xml" -> 1
    """
    
    name = Path(path).name
    return int(''.join(filter(str.isdigit, name)))


def filter_xml(xml_text: str, filter_time: str):

    import xmltodict

    xml_data: dict = xmltodict.parse(xml_text)
    danmaku_list: list = xml_data['i']['d']

    danmaku_time = [int(danmaku['@p'].split(',')[4]) for danmaku in danmaku_list]
    # danmaku: {"@p": metadata, "#text": content}
    # "@p": playtime (seconds?), position (top/bottom), ?, color, timestamp, ?, author, ?, ?

    time_limit = strptimestamp(filter_time)

    print(f'Total danmaku: {len(danmaku_list)}, earliest: {strftimestamp(min(danmaku_time))}, latest: {strftimestamp(max(danmaku_time))}')

    new_danmaku_list = [_danmaku for (_danmaku, _time) in zip(danmaku_list, danmaku_time) if _time < time_limit]
    xml_data['i']['d'] = new_danmaku_list

    print(f'Filter at time: {strftimestamp(time_limit)}, Total danmaku after filter: {len(new_danmaku_list)}')

    return xmltodict.unparse(xml_data)


def filter_danmaku(src_folder: Union[str, Path], dst_folder: Union[str, Path], filter_time: str):

    src_folder, dst_folder = Path(src_folder), Path(dst_folder)

    assert src_folder.exists()
    dst_folder.mkdir(parents=True, exist_ok=True)

    xml_files = list(src_folder.glob('*.xml'))
    try:
        xml_files.sort(key=get_title_number)
    except:
        pass

    def process_file(xmlfile: Path):
        print()  # '\n'
        print(xmlfile)
        result = filter_xml(xmlfile.read_text(encoding='utf-8'), filter_time)
        dstfile = dst_folder.joinpath(xmlfile.name)
        print(dstfile)
        dstfile.write_text(result, encoding='utf-8')

    list(map(process_file, xml_files))
    

def main():
    filter_danmaku('danmaku', 'out', '2023-08-17 17:59:59')
    

if __name__ == '__main__':
    main()

# 1-3
# 2023-06-29
# 4
# 2023-07-06
# 5
# 2023-07-13
# 6
# 2023-07-20
# 7
# 2023-07-27
# 8
# 2023-08-03
# 9
# 2023-08-10
# 10
# 2023-08-17
# 11
# 2023-08-24
# 12
# 2023-08-31
# 13
# 2023-09-14

# 一生を、はじめよう

# MyGO-Danmaku

An archive of BanG Dream! It's MyGO!!!!! danmaku in Bilibili and an script file to filter the danmaku by time to avoid spoiler

这个代码库包含两个部分——MyGO弹幕存档和用时间筛选弹幕的Python脚本

### 其他资源链接

可以使用[KikoPlay](https://github.com/KikoPlayProject/KikoPlay)导入弹幕播放视频，需要分别导入视频资源和弹幕资源。

### 时光机

> 你愿意，**一辈子**喜欢MyGO!!!!!吗

本代码库的“真实”用途，如果屏幕前的你新入坑MyGO，可以按时间筛选弹幕，一定程度上防止剧透。

```python
def main():
    filter_danmaku('danmaku', 'out', '2023-08-17 17:59:59')

if __name__ == '__main__':
    main()
```

如图，`filter_danmaku`接受3个参数分别是存放xml文件的文件夹，输出文件夹和筛选时间。手动修改输出文件夹和输出筛选时间来筛选弹幕，输出为xml文件，保存到指定的输出文件夹（或者`out`）。

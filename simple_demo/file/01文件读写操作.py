# 文件操作的步骤：
# 打开文件 -> 操作文件 -> 关闭文件
# 切记：最后要关闭文件（否则可能会有意想不到的结果）

# 打开文件
# 文件句柄 = open(‘文件路径’, ‘模式’)

# 指定文件编码
# 文件句柄= open(‘文件路径’,’模式’,encoding=’utf-8’)

# 为了防止忘记关闭文件，可以使用上下文管理器来打开文件
# with open(‘文件路径’,’模式’) as 文件句柄:

# 打开文件的模式有：
# r，只读模式（默认）。
# w，只写模式。【不可读；不存在则创建；存在则删除内容；】
# a，追加模式。【可读； 不存在则创建；存在则只追加内容；】
# r+，可读写文件。【可读；可写；可追加】
# w+，写读
# “U”表示在读取时，可以将 \r \n \r\n自动转换成 \n （与 r 或 r+ 模式同使用）

# “b”表示处理二进制文件（如：FTP发送上传ISO镜像文件，linux可忽略，windows处理二进制文件时需标注）

# 关闭文件
# 文件句柄.close()





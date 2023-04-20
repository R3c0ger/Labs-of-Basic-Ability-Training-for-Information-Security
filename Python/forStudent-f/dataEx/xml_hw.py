#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os
from xml.dom import minidom
from xml.dom.minidom import Document

try:
    import xml.etree.cElementTree as et
except ImportError:
    import xml.etree.ElementTree as et

# 题目十六：XML文件的生成和解析
def create_xml(path):
    # 创建XML文档对象
    doc = Document()

    # 创建根节点，添加属性
    tilemap = doc.createElement("tilemap")
    tilemap.setAttribute("tilemapservice", "http://tms.osgeo.org/1.0.0")
    tilemap.setAttribute("version", "1.0.0")
    doc.appendChild(tilemap)  # 将根节点添加到文档对象中

    # 创建title子节点
    title = doc.createElement("title")
    tilemap.appendChild(title)  # 将title节点添加到根节点中
    title_text = doc.createTextNode("default") # 创建文本节点，添加到title节点中
    title.appendChild(title_text)

    # 创建abstract节点
    abstract = doc.createElement("abstract")
    tilemap.appendChild(abstract)

    # 创建srs节点
    srs = doc.createElement("srs")
    tilemap.appendChild(srs)
    srs_text = doc.createTextNode("EPSG:4326")
    srs.appendChild(srs_text)

    # 创建vsrs节点
    vsrs = doc.createElement("vsrs")
    tilemap.appendChild(vsrs)

    # 创建boundingbox节点
    boundingbox = doc.createElement("boundingbox")
    boundingbox.setAttribute("maxx", "180.0")
    boundingbox.setAttribute("maxy", "90.0")
    boundingbox.setAttribute("minx", "-180.0")
    boundingbox.setAttribute("miny", "-90.0")
    tilemap.appendChild(boundingbox)

    # 创建origin节点
    origin = doc.createElement("origin")
    origin.setAttribute("x", "-180.0")
    origin.setAttribute("y", "-90.0")
    tilemap.appendChild(origin)

    # 创建tileformat节点
    tileformat = doc.createElement("tileformat")
    tileformat.setAttribute("extension", "tif")
    tileformat.setAttribute("height", "17")
    tileformat.setAttribute("mime-type", "image/tiff")
    tileformat.setAttribute("width", "17")
    tilemap.appendChild(tileformat)

    # 创建tilesets节点
    tilesets = doc.createElement("tilesets")
    tilesets.setAttribute("profile", "global-geodetic")
    tilemap.appendChild(tilesets)

    # 创建tilesets的子节点tileset
    units_per_pixel = [10.588, 5.294, 2.647, 1.323, 0.661, 0.331]
    for i in range(len(units_per_pixel)): # range(6)，考虑兼容
        tileset = doc.createElement("tileset")
        tileset.setAttribute("href", "")
        tileset.setAttribute("order", str(i))
        tileset.setAttribute("units-per-pixel", str(units_per_pixel[i])) # str(10.588 / (2 ** i))
        tilesets.appendChild(tileset)

    # 打开文件，写入XML文档对象
    with open(path, 'w') as f:
        doc.writexml(f, indent='', addindent='\t', newl='\n', encoding="utf-8")
        # indent：根节点前缩进，addindent：子节点前缩进，newl：换行符，encoding：编码

def parse_xml(path):
    # 参数判断，检查文件是否存在，若不存在则返回空字典
    if not os.path.exists(path):
        return {}

    # 解析XML文件，从文件中导入数据
    tree = et.parse(path)
    root = tree.getroot()

    result_dict = dict()
    # 获取根节点的tilemapservice属性对应的值
    if 'tilemapservice' in root.attrib:
        result_dict["tilemap service"] = root.attrib.get("tilemapservice", "")
    # 查找带有title标签的子节点，获取其文本值
    title_node = root.find("title")
    if title_node is not None:
        result_dict["title"] = title_node.text
    # 获取tileset标签的子节点数量
    tilesets = root.findall(".//tileset") # XPath支持，查找带有tileset标签的子节点，获取其列表
    if tilesets is not None:
        result_dict["tileset count"] = len(tilesets)
    # 获取tileset标签的子节点中order属性的最大值
        max_order = max(int(node.attrib.get('order', -1)) for node in tilesets) # order值最小为0
        if max_order >= 0:
            result_dict["tileset max"] = max_order

    return result_dict


if __name__ == "__main__":
    create_xml("./created.xml")
    print(parse_xml("./created.xml"))
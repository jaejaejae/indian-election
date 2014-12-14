import numpy
import random
import matplotlib.patches as matpatch
def loadGeo(geo_file):
    f_in = open(geo_file,'r')
    tab = {}
    for line in f_in.readlines():
        lst = line.split()
        msg_id = lst[0]
        msg_geo = lst[1].split(',')
        tab[msg_id]=msg_geo
    return tab

def findNearId(la, lo):
    la = float(la)
    lo = float(lo)
    lat = [17.38,13.08,12.98,19.07,22.57,26.84,26.91,28.63,21.15,22.72,27.16,21.66,26.02,9.92]
    lon = [78.49,80.28,77.61,72.88,88.34,80.95,75.78,77.25,79.08,75.86,78.01,83.59,73.85,78.12]
    min_dis = 1000000000
    ret = -1
    for idx,val in enumerate(lat):
        tmp_lat = float(val)
        tmp_lon = float(lon[idx])
        tmp_dis = (tmp_lat-la)*(tmp_lat-la) + (tmp_lon - lo)*(tmp_lon - lo)
        if tmp_dis < min_dis:
            min_dis = tmp_dis
            ret = idx
    return ret 

def is_number(s):
    if s == 'NaN':
        return False
    try:
        float(s)
        return True
    except ValueError:
        return False

def plot(text, size):
    from mpl_toolkits.basemap import Basemap
    import matplotlib.pyplot as plt
    #from matplotlib.font_manager import FontProperties
    
    #fontP = FontProPerties()
    #fontP.set_size('small')
    # setup Lambert Conformal basemap.
    m = Basemap(width=3000000,height=3000000,projection='lcc',
                resolution='c',lat_0=18,lon_0=78)
    m.drawcoastlines()
    #m.fillcontinents(color='coral',lake_color='aqua')
    m.shadedrelief()
    colors = numpy.random.rand(30,3)
    #lengend
    handles = []
    for i in range(30):
        patch = matpatch.Patch(color = colors[i], label='Topic ' + str(i+1))
        handles.append(patch)
    plt.legend(handles = handles,  bbox_to_anchor=(1.2, 1.0),  prop={'size':10})
    lat = [17.38,13.08,12.98,19.07,22.57,26.84,26.91,28.63,21.15,22.72,27.16,21.66,26.02,9.92]
    lon = [78.49,80.28,77.61,72.88,88.34,80.95,75.78,77.25,79.08,75.86,78.01,83.59,73.85,78.12]
    df_x = [0.35,-0.25,-0.35,0.25,0]
    df_y = [0.35,0.25,-0.25,-02.5,0]
    f_lat = []
    f_lon = []
    f_size = []
    f_color = []
    random.seed()
    for place_id in range(len(lat)):
        for i in range(5):
            #f_lat.append(lat[place_id] + df_y[i])
            f_lat.append(lat[place_id] + 3*(random.random()-0.5))
            f_lon.append(lon[place_id] + 3*(random.random()-0.5))
            #f_lon.append(lon[place_id] + df_x[i])
            f_size.append(size[place_id][i]*15)
            f_color.append(colors[text[place_id][i]])
            #m.plot(lon[place_id]+df_y[i],lat[place_id]+ df_x[i], 'bo',markersize = size[place_id][i], latlon = True)
    m.scatter(f_lon, f_lat, s = f_size, c = f_color, alpha = 0.5, latlon = True)
    m.scatter(lon, lat, s = 8000, c = 'b', alpha = 0.1, latlon = True)
    #m.scatter(f_lon, f_lat, s = f_size, c = f_color, latlon = True)
    #m.plot(f_lon,f_lat,'bo',markersize = 5, latlon = True)
    plt.show()


def main():
    tab = loadGeo('geo.txt')
    topic_num = 30
    place_num = 14 
    ret = []
    ret_topic = []
    for place in range(place_num):
        ch = [0.0]*topic_num
        ch_topic = range(topic_num)
        ret_topic.append(ch_topic)
        ret.append(ch)
    f_in = open('modi.csv','r')
    for line in f_in.readlines():
        lst = line.split(',')
        msg_id = lst[0]
        print len(lst)
        freq = lst[1::]
        if tab.has_key(msg_id):
            lat, lon = tab[msg_id]
            place_id = findNearId(lat, lon)
            for i,score in enumerate(freq):
                if is_number(score):
                    ret[place_id][i] += float(score)
    ret_top_three = []
    ret_size_three = []
    for place in range(place_num):
        ret_topic[place].sort( key = lambda x: ret[place][x], reverse = True)
        #print ret_topic[place]
        #print ret[place]
        print place
        print '---------------------'
        top_three = ret_topic[place][0:5]
        ret_top_three.append(top_three)
        print top_three
        size_three = map(lambda x: ret[place][x], top_three)
        ret_size_three.append(size_three)
        print size_three
        print '---------------------'
    plot(ret_top_three, ret_size_three)
    f_in.close()

if __name__ == '__main__':
    main()

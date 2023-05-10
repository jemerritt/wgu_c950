import csv

from hashtable import ChainHash

package_hash = ChainHash()
package_tracker = []
initialized = False

# Read package info from csv file and insert into hash table
# O(N^2)
with open('./data/packages.csv') as csv_f:
    imp_csv = csv.reader(csv_f, delimiter=';')
    for row in imp_csv:
        package_id = int(row[0])
        address = row[1]
        city = row[2]
        zip_code = row[4]
        deadline = row[5]
        weight = row[6]
        note = row[7]
        address_id = 0
        status = ''
        time = ''

        package = [package_id, address, city, zip_code, deadline, weight, note, address_id, status, time]

        package_hash.insert(package_id, package)

    # Returns the associated package ID for given key
    # O(N)
    def get_package_id(key):
        return package_hash.search(key)[0]

    # Returns the associated address ID for given key
    # O(N)
    def get_package_address_id(key):
        return package_hash.search(key)[7]

    # Returns the full package values for given key
    # O(N)
    def get_value(key):
        return package_hash.search(key)[0], package_hash.search(key)[1], package_hash.search(key)[2],\
            package_hash.search(key)[3], package_hash.search(key)[4], package_hash.search(key)[5],\
            package_hash.search(key)[6], package_hash.search(key)[7], package_hash.search(key)[8],\
            package_hash.search(key)[9]

    # Updates status of package and adds package details to tracking list
    # O(N)
    def change_status(key, stat, time_value):
        package_hash.update_status(key, stat, time_value)
        package_to_track = get_value(key)
        package_tracker.append(package_to_track)

    # Sets the address id for package with given key
    # O(N)
    def change_address_id(key, value):
        package_hash.update_address_id(key, value)

    # Uses given key and timestamp to return package with the latest time
    # that is before or equal to timestamp
    # O(N)
    def find_closest_to_ts(key, ts):
        check_closest = []
        for inx in package_tracker:
            time_int = int(inx[9].replace(":", ""))
            if inx[0] == key and time_int <= ts:
                package_times = [time_int, package_tracker.index(inx)]
                check_closest.append(package_times)
        check_closest.sort()
        rtn_package = check_closest.pop()
        return rtn_package

    # Returns all packages relative to the given timestamp
    # O(N^2)
    def get_all_packages_at(ts):
        packages_at_time = []
        for idx in range(1, 41):
            package_to_add = find_closest_to_ts(idx, ts)
            packages_at_time.append(package_tracker[package_to_add[1]])
        return packages_at_time

    # Returns package relative to the given timestamp and package id
    # O(N)
    def get_package_at(pkg_id, ts):
        package_at_time = []
        package_to_add = find_closest_to_ts(pkg_id, ts)
        package_at_time.append(package_tracker[package_to_add[1]])
        return package_at_time

    # Initialize all packages as at the hub for start of day and add entries to package tracker
    # O(N^2)
    if not initialized:
        for i in range(1, 41):
            change_status(i, "at the hub:  ", '08:00:00')
            initialized = True

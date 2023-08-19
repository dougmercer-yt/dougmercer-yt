# These functions were taken from https://github.com/sampottinger/py_common_subseq .

def add_matched_element(element, target_set, sep):
    """Append an element to the end of all elements in a set.
    Creates a new copy of target_set with an element appended to the end of all
    items in that target_set. Returns a union between the target_set and the
    newly created copy of target_set.
    @param element: The element to add.
    @param target_set: Collection of items to append element to.
    @type target_set: set
    @return: The union between a copy of target_set with element appended to
        all of its items and the original target_set.
    @rtype: set
    """
    new_elements = map(lambda x: x + sep + element, target_set)
    return target_set.union(new_elements)


def find_common_subsequences(seq_1, seq_2, sep='', empty_val=''):
    """Find the number of common subsequences between two collections.
    This function finds the common subsequences between two collections and
    returns an actual listing of those subsequences. This is less space
    efficient (O(len(seq_1)^2)) than count_common_subsequences.
    > subsequences = find_common_subsequences('qwer', 'qewr')
    > print subsequences
    set(['', 'qer', 'wr', 'qwr', 'er', 'qr', 'e', 'qw', 'q', 'r', 'qe', 'w'])
    @param seq_1: The first collection to find subsequences in.
    @type seq_1: Any integer indexable collection (list, tuple, etc.)
    @param seq_2: The second collection to find subsequences in.
    @type seq_2: Any integer indexable collection (list, tuple, etc.)
    @keyword sep: Seperator to put between elements when constructing a
        subsequence. Defaults to ''.
    @keyword empty_val: The value to use to represent the empty set.
    @return: Set of subsequences in common between seq_1 and seq_2.
    @rtype: set
    """
    # Ensure the smaller of the two sequences is used to create the columns for
    # the DP table.
    if len(seq_1) < len(seq_2):
        new_seq_1 = seq_2
        seq_2 = seq_1
        seq_1 = new_seq_1

    # Use length plus one to provide a row and column in the subsequence table,
    # a row / column not corresponding to an element. This provides
    # initialization values to the algorithm and handles the edge case of
    # calculating an element in the subsequence table when that element is
    # either in the first row of the table or is the first element of a row.
    # This also includes / handles the empty string as a substring.
    seq_1_len = len(seq_1)
    seq_2_len = len(seq_2)
    seq_1_len_plus_1 = seq_1_len + 1
    seq_2_len_plus_1 = seq_2_len + 1
    
    # Initialize the first two rows of a "2D array" consisting of
    # seq_1_len_plus_1 by seq_2_len_plus_1 values. Note that, due to space
    # optimizations, only two rows are ever maintained in memory.
    subseq_last_row = [set([empty_val])] * seq_2_len_plus_1
    subseq_current_row = [set([empty_val])] + [set()] * seq_2_len

    for row in range(1, seq_1_len_plus_1):

        for col in range(1, seq_2_len_plus_1):

            if seq_1[row-1] == seq_2[col-1]:
                diagonal_cell_value = subseq_last_row[col - 1]
                matched_element = seq_1[row-1]
                new_cell_value = add_matched_element(matched_element,
                    diagonal_cell_value, sep)
            else:
                above_set = subseq_last_row[col]
                left_set = subseq_current_row[col-1]
                new_cell_value = above_set.union(left_set)
            subseq_current_row[col] = new_cell_value

        subseq_last_row = subseq_current_row
        subseq_current_row = [set([empty_val])] + [set()] * seq_2_len

    return subseq_last_row[seq_2_len]

print(
    *sorted(
        find_common_subsequences("SLUBSCRIKBE", "SULIBSCKRIBE"),
        key=len,
        reverse=True,
    ),
    sep="\n",
)

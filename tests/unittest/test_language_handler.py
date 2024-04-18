
# Generated by CodiumAI

from mergemate.algo.language_handler import sort_files_by_main_languages

"""
Code Analysis

Objective:
The objective of the function is to sort a list of files by their main language, putting the files that are in the main 
language first and the rest of the files after. It takes in a dictionary of languages and their sizes, and a list of 
files.

Inputs:
- languages: a dictionary containing the languages and their sizes
- files: a list of files

Flow:
1. Sort the languages by their size in descending order
2. Get all extensions for the languages
3. Filter out files with bad extensions
4. Sort files by their extension, putting the files that are in the main extension first and the rest of the files after
5. Map languages_sorted to their respective files
6. Append the files to the files_sorted list
7. Append the rest of the files to the files_sorted list under the "Other" language category
8. Return the files_sorted list

Outputs:
- files_sorted: a list of dictionaries containing the language and its respective files

Additional aspects:
- The function uses a language_extension_map dictionary to map the languages to their respective extensions
- The function uses the filter_bad_extensions function to filter out files with bad extensions
- The function uses a rest_files dictionary to store the files that do not belong to any of the main extensions
"""


class TestSortFilesByMainLanguages:
    # Tests that files are sorted by main language, with files in main language first and the rest after
    def test_happy_path_sort_files_by_main_languages(self):
        languages = {'Python': 10, 'Java': 5, 'C++': 3}
        files = [
            type('', (object,), {'filename': 'file1.py'})(),
            type('', (object,), {'filename': 'file2.java'})(),
            type('', (object,), {'filename': 'file3.cpp'})(),
            type('', (object,), {'filename': 'file4.py'})(),
            type('', (object,), {'filename': 'file5.py'})()
        ]
        expected_output = [
            {'language': 'Python', 'files': [files[0], files[3], files[4]]},
            {'language': 'Java', 'files': [files[1]]},
            {'language': 'C++', 'files': [files[2]]},
            {'language': 'Other', 'files': []}
        ]
        assert sort_files_by_main_languages(languages, files) == expected_output

    # Tests that function handles empty languages dictionary
    def test_edge_case_empty_languages(self):
        languages = {}
        files = [
            type('', (object,), {'filename': 'file1.py'})(),
            type('', (object,), {'filename': 'file2.java'})()
        ]
        expected_output = [{'language': 'Other', 'files': files}]
        assert sort_files_by_main_languages(languages, files) == expected_output

    # Tests that function handles empty files list
    def test_edge_case_empty_files(self):
        languages = {'Python': 10, 'Java': 5}
        files = []
        expected_output = [
            {'language': 'Other', 'files': []}
        ]
        assert sort_files_by_main_languages(languages, files) == expected_output

    # Tests that function handles languages with no extensions
    def test_edge_case_languages_with_no_extensions(self):
        languages = {'Python': 10, 'Java': 5, 'C++': 3}
        files = [
            type('', (object,), {'filename': 'file1.py'})(),
            type('', (object,), {'filename': 'file2.java'})(),
            type('', (object,), {'filename': 'file3.cpp'})()
        ]
        expected_output = [
            {'language': 'Python', 'files': [files[0]]},
            {'language': 'Java', 'files': [files[1]]},
            {'language': 'C++', 'files': [files[2]]},
            {'language': 'Other', 'files': []}
        ]
        assert sort_files_by_main_languages(languages, files) == expected_output

    # Tests the behavior of the function when all files have bad extensions and only one new valid file is added.
    def test_edge_case_files_with_bad_extensions_only(self):
        languages = {'Python': 10, 'Java': 5, 'C++': 3}
        files = [
            type('', (object,), {'filename': 'file1.csv'})(),
            type('', (object,), {'filename': 'file2.pdf'})(),
            type('', (object,), {'filename': 'file3.py'})()  # new valid file
        ]
        expected_output = [{'language': 'Python', 'files': [files[2]]}, {'language': 'Other', 'files': []}]
        assert sort_files_by_main_languages(languages, files) == expected_output

    # Tests general behaviour of function
    def test_general_behaviour_sort_files_by_main_languages(self):
        languages = {'Python': 10, 'Java': 5, 'C++': 3}
        files = [
            type('', (object,), {'filename': 'file1.py'})(),
            type('', (object,), {'filename': 'file2.java'})(),
            type('', (object,), {'filename': 'file3.cpp'})(),
            type('', (object,), {'filename': 'file4.py'})(),
            type('', (object,), {'filename': 'file5.py'})(),
            type('', (object,), {'filename': 'file6.py'})(),
            type('', (object,), {'filename': 'file7.java'})(),
            type('', (object,), {'filename': 'file8.cpp'})(),
            type('', (object,), {'filename': 'file9.py'})()
        ]
        expected_output = [
            {'language': 'Python', 'files': [files[0], files[3], files[4], files[5], files[8]]},
            {'language': 'Java', 'files': [files[1], files[6]]},
            {'language': 'C++', 'files': [files[2], files[7]]},
            {'language': 'Other', 'files': []}
        ]
        assert sort_files_by_main_languages(languages, files) == expected_output
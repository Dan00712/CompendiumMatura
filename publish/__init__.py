


def main():
    import publish.compile_to_html as to_html
    import publish.prepare_to_publish as prepare 
    import publish.github_pages as export
    
    if to_html.main() != 0: return 1
    if prepare.main() != 0: return 2
    if export.main() != 0: return 3
    return 0


if __name__ == '__main__':
    exit(main())
# Spider

!!! This is just a small project to help me understand more about web crawling, how it works, what knowledge is needed,

----------------
# Web crawling basic: Spider (pure standard library)

* Libraries used:

- urllib.request / urlopen: fetch HTML over HTTP(S).

- urllib.parse (urljoin, urlparse): normalize relative URLs to absolute; extract host/domain.

- html.parser.HTMLParser: event-driven (SAX) parser to capture <a href=...>.

- threading: multi-threading for I/O-bound work (many concurrent requests).

- queue.Queue: thread-safe queue (producer–consumer model for URLs to crawl).

- os / os.path: create the project directory; check/write state files.

* Notable techniques:

- Event-driven parsing (SAX): subclass HTMLParser, override handle_starttag to collect href quickly—lightweight and lower RAM than building the full DOM tree.

- Link normalization & filtering:

      Use urljoin(...) to convert relative links to absolute.

      Drop #fragment to avoid “virtual” duplicate URLs.

      Filter by domain to limit the crawl scope.

- Deduplication with set: both queue and crawled are sets → inherent dedupe, O(1) lookups.

- Multithreading for I/O-bound tasks:

     Worker pool: N threads pull URLs from queue.Queue() and crawl.

     Use queue.join() to synchronize the completion of a “batch” of work.

- Persistence (resumable):

    queue.txt / crawled.txt store state → you can resume after stopping.

    Write in sorted order for stable logs/diffs.

- Near-BFS traversal: frontier (queue) + visited (crawled) yields a breadth-first-like sweep, reducing revisits.

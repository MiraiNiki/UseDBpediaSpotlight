import spotlight
annotations = spotlight.annotate('http://localhost/rest/annotate',
                                 'President Obama on Monday will call for a new minimum tax rate for individuals making more than $1 million a year to ensure that they pay at least the same percentage of their earnings as other taxpayers, according to administration officials.',
                                 confidence=0.4, support=20)

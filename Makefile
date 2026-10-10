.PHONY: check

check:  ## tier 0 static gate: index.html + CNAME are well formed (offline)
	python3 check.py

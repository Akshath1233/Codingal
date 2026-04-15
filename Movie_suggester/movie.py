import time, pandas as pd
from unicodedata import name
from textblob import TextBlob
from colorama import init, Fore

init(autoreset=True)

try: df=pd.read_csv(r"C:\Users\Aksha\OneDrive\Desktop\Coding\Codingal\Movie_suggester\imdb_top_1000.csv")
except FileNotFoundError:
    print(Fore.RED + "Error: The file 'imdb_top_1000.csv' was not found."); raise SystemExit

genres = sorted({g.strip() for xs in df["Genre"].dropna().str.split(", ") for g in xs})

def dots():
    for _ in range(3): print(Fore.YELLOW + ".", end="", flush=True); time.sleep(0.5)

def senti(p): return "Positive" if p>0 else "Negative" if p<0 else "Neutral"

def recommend(genre=None, mood=None, rating=None, n=5):
    d = df
    if genre: d = d[d["Genre"].str.contains(genre, case=False, na=False)]
    if rating is not None: d = d[d["IMDB_Rating"] >= rating]
    if d.empty: return "No suitable movie recommendations found."
    d,need_nonneg, out = d.sample(frac=1).reset_index(drop=True), bool(mood), []
    for _, r in d.iterrows():
        ov = r.get("Overview")
        if pd.isna(ov): continue
        pol = TextBlob(ov).sentiment.polarity
        if (not need_nonneg) or pol >= 0:
            out.append((r["Series_Title"], pol))
            if len(out) == n: break
    return out if out else "No suitable movie recommendations found."
def show(recs, name):
    print(Fore.YELLOW + f"\n f AI-Analyzed Movie Recommendations for {name}:")
    for i, (t, p) in enumerate(recs, 1):
        print(f"{Fore.CYAN}{i}. {t} (Polarity: {p :. 2f}, {senti(p)})")
        return out if out else "No suitable movie recommendations found."
def show(recs, name):
    print(Fore.YELLOW + f"\n f AI-Analyzed Movie Recommendations for {name}:")
    for i, (t, p) in enumerate(recs, 1):
        print(f"{Fore.CYAN}{i}. {t} (Polarity: {p :. 2f}, {senti(p)})")

def get_genre():
    print(Fore.GREEN + "Available Genres: ", end="")
    for i, g in enumerate(genres, 1): print(f"{Fore.CYAN}{i}. {g}")
print()
while True:
x = input(Fore. YELLOW + "Enter genre number or name: ") .strip()
if x.isdigit() and 1 <= int(x) <= len(genres): return genres[int(x) - 1]
x = x.title()
if x in genres: return x
print(Fore.RED + "Invalid input. Try again. \n")
   
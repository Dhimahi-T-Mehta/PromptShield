from presidio_analyzer import AnalyzerEngine

analyzer = AnalyzerEngine()

results = analyzer.analyze(
    text="My email is test@gmail.com",
    language="en"
)

print(results)
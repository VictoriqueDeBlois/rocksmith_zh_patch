"""Offline behavioral regression tests; never substitutes for the live sample."""
import tempfile
import unittest
from pathlib import Path

from .cli import select
from .prompts import build_prompts
from .router import route
from .runner import map_response, run, validate

class ProofreaderTests(unittest.TestCase):
    def test_routes(self):
        examples = {"SKIP": ["{0}{C}[1]", "Am7", "EMaj7", "HW-100B", "640x480", "Epiphone® Les Paul"],
                    "A": ["CANCEL", "MEDIUM"], "B": ["Slide your finger along the string"],
                    "C": ["Score at least [1] points on a single string"],
                    "D": ["Your online profile could not be found"],
                    "E": ["Session Drums", "Classic fuzz pedal"],
                    "F": ["Unable to save your settings"], "G": ["There is always something new to discover."]}
        for category, sources in examples.items():
            for source in sources:
                with self.subTest(source=source):
                    self.assertEqual(route(source), category)

    def test_validation(self):
        self.assertFalse(validate("{0}{C}[1]{C}", "你好{0}{C}[1]{C}"))
        for text in ("你好{C}{0}[1]{C}", "你好{0}{C}[1]", "", "你好,", "你好\n", "你好\\n"):
            self.assertTrue(validate("{0}{C}[1]{C}", text))
        self.assertTrue(validate("Profile", "配置文件", "玩家档案", "D"))
        self.assertTrue(validate("Warm Pad", "Warm Pad", "温暖铺底音色", "E"))
        self.assertTrue(validate("Warm Pad", "温暖 Pad", "温暖铺底音色", "E"))
        self.assertTrue(validate("LO MID Q", "中低频 Q 值", "中低频Q值", "E"))
        self.assertTrue(validate("cross button", "十字键", "叉键", "A"))
        self.assertTrue(validate("Score Attack", "得分攻击", "得分挑战", "C"))
        self.assertTrue(validate("in a game", "在一局游戏中", "在单局游戏中", "C", "更符合中文习惯"))
        self.assertTrue(validate("Combo", "一体式音箱", "连击", "E"))

    def test_response_ids(self):
        items = [{"id": "1"}, {"id": "2"}]
        self.assertEqual(list(map_response(items, {"translations": [{"id": "2", "text": "二"}, {"id": "1", "text": "一"}]})), ["2", "1"])
        for rows in ([{"id": "1", "text": "一"}] * 2,
                     [{"id": "3", "text": "一"}, {"id": "2", "text": "二"}], []):
            with self.assertRaises(ValueError):
                map_response(items, {"translations": rows})

    def test_sampling(self):
        items = [dict(id=f"{c}{i}", category=c) for c in "ABCDEFG" for i in range(40)]
        sample = select(items, 200, 42, 20)
        self.assertEqual(sample, select(list(reversed(items)), 200, 42, 20))
        self.assertEqual(len({i["id"] for i in sample}), 200)
        self.assertTrue(all(sum(i["category"] == c for i in sample) >= 20 for c in "ABCDEFG"))

    def test_resume_rejection_failure_and_staleness(self):
        items = [dict(id=str(i), source="{0} Text", translation="{0} 文本", category="G") for i in range(3)]
        workers = [dict(name="test", model="fake", endpoint="fake", concurrency=2, batch_size=2)]
        calls = []
        def request(worker, prompt, batch):
            calls.append(batch)
            if any(i["id"] == "2" for i in batch):
                raise OSError("offline")
            return {i["id"]: {"text": "bad", "reason": "test"} for i in batch}
        with tempfile.TemporaryDirectory() as directory:
            out = Path(directory) / "out.json"
            done, errors = run(items, workers, build_prompts(), out, request)
            self.assertEqual(len(done), 2)
            self.assertEqual(set(errors), {"2"})
            self.assertTrue(all(i["revised"] == i["translation"] and i["rejection"] for i in done.values()))
            calls.clear()
            run(items, workers, build_prompts(), out, request)
            self.assertEqual([i["id"] for b in calls for i in b], ["2"])
            with self.assertRaises(ValueError):
                run(items[:1], workers, build_prompts(), out, request)

if __name__ == "__main__":
    unittest.main()

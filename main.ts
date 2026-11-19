// gta6-meme-x-01 entry program (Node 22, standard library only).
//
// The entry is the X post itself: the house reads the post from X (its first
// picture and its text) and hands that to the judge. This program only hands
// the post's address to the gate: it copies POST.json from the repository
// root to /output/POST.json, byte for byte, and does nothing else.
//
// Run the way the grader does:
//   mkdir -p out && MAKEFUN_BOT_DIR=. MAKEFUN_OUTPUT_DIR=out node main.ts

import { copyFileSync, mkdirSync } from "node:fs";
import { join } from "node:path";

const botDir = process.env.MAKEFUN_BOT_DIR ?? "/bot";
const outputDir = process.env.MAKEFUN_OUTPUT_DIR ?? "/output";

mkdirSync(outputDir, { recursive: true });

const source = join(botDir, "POST.json");
const target = join(outputDir, "POST.json");
try {
  copyFileSync(source, target);
} catch (error) {
  console.error(`could not copy POST.json from ${botDir}: ${(error as Error).message}`);
  process.exit(1);
}

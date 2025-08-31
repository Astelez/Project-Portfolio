# Forensic Disk Analysis — E3 + Autopsy

**Goal**: Acquire a disk image, preserve chain of custody, perform analysis in E3/Autopsy, and produce a concise, professional case report.

## Scope
- Media: VM disk / USB drive you own
- Objectives: file recovery, timeline analysis, indicators of deleted/hidden data

## Workflow (High Level)
1. **Acquisition**: Use FTK Imager or `dd` to create an image (E01/raw). Compute hashes.
2. **Verification**: Validate hash integrity, document chain of custody.
3. **Analysis**: E3 + Autopsy (recovered files, timelines, metadata, browser artifacts).
4. **Reporting**: Write findings and attach evidence references.

## Commands (Example)
```bash
# Raw image with dd (lab demo)
sudo dd if=/dev/sdX of=evidence/disk.img bs=4M status=progress
sha256sum evidence/disk.img > evidence/disk.img.sha256
```

## Deliverables
- `case_report.md` (or PDF)
- `chain_of_custody.md`
- Hashes and logs in `evidence/`
- Screenshots/artifacts in `artifacts/`

## What I Learned (fill this in)
- TODO: acquisition pitfalls
- TODO: timeline correlation
- TODO: report clarity for non-technical readers
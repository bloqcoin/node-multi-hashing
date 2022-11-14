{
    "targets": [
        {
            "target_name": "multihashing",
            "sources": [
                "src/multihashing.cc",
                "src/sha256d.c",
                "src/crypto/sha256.c"
            ],
            "include_dirs": [
                "src/crypto",
                "<!(node -e \"require('nan')\")"
            ],
            "cflags_cc": [
                "-std=c++14"
            ],
        }
    ]
}

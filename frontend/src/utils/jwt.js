// ============================================================
// Decode JWT Payload
// ============================================================

export function decodeToken(token) {

    try {

        if (!token) {
            return null;
        }

        const payload = token.split(".")[1];

        const decoded = atob(payload);

        return JSON.parse(decoded);

    } catch {

        return null;

    }

}

// ============================================================
// Check Expiration
// ============================================================

export function isTokenExpired(token) {

    const payload = decodeToken(token);

    if (!payload || !payload.exp) {

        return true;

    }

    const currentTime = Math.floor(Date.now() / 1000);

    return payload.exp < currentTime;

}

// ============================================================
// Safe Payload Getter
// ============================================================

export function getTokenPayload(token) {

    if (!token) {

        return null;

    }

    if (isTokenExpired(token)) {

        return null;

    }

    return decodeToken(token);

}
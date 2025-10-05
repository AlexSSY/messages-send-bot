export async function sendCodeRequest(phoneNumber) {
  try {
    const response = await fetch("/api/auth/send-code", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        "X-Telegram-Init-Data": window.Telegram.WebApp.initData,
      },
      body: JSON.stringify({
        phone_number: phoneNumber
      }),
    });

    if (!response.ok) {
      alert(`HTTP error! status: ${response.status}`);
    }

    return await response.json();
  } catch (err) {
    alert("Ошибка: " + err.message);
  }

  return false
}

export async function verifyCode(code, phoneNumber, phoneCodHash) {
  try {
    const response = await fetch("/api/auth/verify-code", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        "X-Telegram-Init-Data": window.Telegram.WebApp.initData,
      },
      body: JSON.stringify({
        code: code,
        phone_number: phoneNumber,
        phone_code_hash: phoneCodHash
      }),
    });

    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }

    const data = await response.json();
    return data.status
  } catch (err) {
    console.error("Error:", err);
    alert("Ошибка: " + err.message);
    return false
  }
}

export async function signInWith2fa() {
  
}
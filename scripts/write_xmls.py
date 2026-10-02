import os

files = {
    r'D:\SentinelX360\android-app\app\src\main\res\layout\activity_login.xml': '''<?xml version="1.0" encoding="utf-8"?>
<androidx.constraintlayout.widget.ConstraintLayout
    xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:app="http://schemas.android.com/apk/res-auto"
    xmlns:tools="http://schemas.android.com/tools"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:background="@color/bg_deep_navy"
    tools:context=".presentation.ui.auth.LoginActivity">

    <ScrollView
        android:layout_width="match_parent"
        android:layout_height="match_parent"
        android:fillViewport="true"
        android:scrollbars="none">

        <LinearLayout
            android:layout_width="match_parent"
            android:layout_height="wrap_content"
            android:orientation="vertical"
            android:padding="24dp"
            android:gravity="center_horizontal">

            <View
                android:layout_width="match_parent"
                android:layout_height="32dp" />

            <TextView
                android:layout_width="wrap_content"
                android:layout_height="wrap_content"
                android:text="SentinelX 360"
                android:textSize="32sp"
                android:fontFamily="sans-serif-black"
                android:letterSpacing="0.03"
                android:textColor="@color/text_primary"
                android:layout_marginBottom="4dp" />

            <TextView
                android:layout_width="wrap_content"
                android:layout_height="wrap_content"
                android:text="SECURE DIGITAL PAYMENTS"
                android:textSize="11sp"
                android:fontFamily="sans-serif-medium"
                android:letterSpacing="0.15"
                android:textColor="@color/primary_cyan"
                android:layout_marginBottom="48dp" />

            <LinearLayout
                android:layout_width="match_parent"
                android:layout_height="wrap_content"
                android:orientation="vertical"
                android:gravity="start">

                <TextView
                    android:layout_width="wrap_content"
                    android:layout_height="wrap_content"
                    android:text="Welcome Back"
                    android:textSize="24sp"
                    android:fontFamily="sans-serif-medium"
                    android:letterSpacing="0.01"
                    android:textColor="@color/text_primary"
                    android:layout_marginBottom="6dp" />

                <TextView
                    android:layout_width="wrap_content"
                    android:layout_height="wrap_content"
                    android:text="Secure login to continue"
                    android:textSize="14sp"
                    android:fontFamily="sans-serif"
                    android:textColor="@color/text_hint"
                    android:layout_marginBottom="32dp" />

                <com.google.android.material.textfield.TextInputLayout
                    android:id="@+id/tilEmail"
                    style="@style/Widget.MaterialComponents.TextInputLayout.OutlinedBox"
                    android:layout_width="match_parent"
                    android:layout_height="wrap_content"
                    android:layout_marginBottom="16dp"
                    app:boxBackgroundColor="@color/bg_surface"
                    app:boxStrokeColor="@color/border_focus"
                    app:boxCornerRadiusBottomEnd="12dp"
                    app:boxCornerRadiusBottomStart="12dp"
                    app:boxCornerRadiusTopEnd="12dp"
                    app:boxCornerRadiusTopStart="12dp"
                    app:hintTextColor="@color/primary_cyan"
                    android:textColorHint="@color/text_hint">

                    <com.google.android.material.textfield.TextInputEditText
                        android:id="@+id/etEmail"
                        android:layout_width="match_parent"
                        android:layout_height="wrap_content"
                        android:hint="Email / UPI ID"
                        android:fontFamily="sans-serif"
                        android:inputType="textEmailAddress"
                        android:textColor="@color/text_primary"
                        android:padding="16dp" />
                </com.google.android.material.textfield.TextInputLayout>

                <com.google.android.material.textfield.TextInputLayout
                    android:id="@+id/tilPassword"
                    style="@style/Widget.MaterialComponents.TextInputLayout.OutlinedBox"
                    android:layout_width="match_parent"
                    android:layout_height="wrap_content"
                    android:layout_marginBottom="32dp"
                    app:passwordToggleEnabled="true"
                    app:passwordToggleTint="@color/text_secondary"
                    app:boxBackgroundColor="@color/bg_surface"
                    app:boxStrokeColor="@color/border_focus"
                    app:boxCornerRadiusBottomEnd="12dp"
                    app:boxCornerRadiusBottomStart="12dp"
                    app:boxCornerRadiusTopEnd="12dp"
                    app:boxCornerRadiusTopStart="12dp"
                    app:hintTextColor="@color/primary_cyan"
                    android:textColorHint="@color/text_hint">

                    <com.google.android.material.textfield.TextInputEditText
                        android:id="@+id/etPassword"
                        android:layout_width="match_parent"
                        android:layout_height="wrap_content"
                        android:hint="Password"
                        android:fontFamily="sans-serif"
                        android:inputType="textPassword"
                        android:textColor="@color/text_primary"
                        android:padding="16dp" />
                </com.google.android.material.textfield.TextInputLayout>

                <FrameLayout
                    android:layout_width="match_parent"
                    android:layout_height="56dp"
                    android:layout_marginBottom="24dp">
                    
                    <com.google.android.material.button.MaterialButton
                        android:id="@+id/btnLogin"
                        android:layout_width="match_parent"
                        android:layout_height="match_parent"
                        android:text="LOGIN"
                        android:textSize="15sp"
                        android:fontFamily="sans-serif-medium"
                        android:letterSpacing="0.08"
                        app:cornerRadius="12dp"
                        app:backgroundTint="@color/primary_cyan"
                        android:textColor="@color/white"
                        android:stateListAnimator="@null" />
                        
                    <ProgressBar
                        android:id="@+id/progressBar"
                        android:layout_width="24dp"
                        android:layout_height="24dp"
                        android:layout_gravity="center"
                        android:visibility="gone"
                        android:indeterminateTint="@color/white" />
                </FrameLayout>

                <LinearLayout
                    android:layout_width="match_parent"
                    android:layout_height="wrap_content"
                    android:orientation="horizontal"
                    android:gravity="center"
                    android:layout_marginBottom="24dp">
                    
                    <View
                        android:layout_width="0dp"
                        android:layout_height="1dp"
                        android:layout_weight="1"
                        android:background="@color/border_color" />
                        
                    <TextView
                        android:layout_width="wrap_content"
                        android:layout_height="wrap_content"
                        android:text="OR"
                        android:fontFamily="sans-serif-medium"
                        android:textColor="@color/text_secondary"
                        android:textSize="12sp"
                        android:layout_marginHorizontal="16dp" />
                        
                    <View
                        android:layout_width="0dp"
                        android:layout_height="1dp"
                        android:layout_weight="1"
                        android:background="@color/border_color" />
                </LinearLayout>

                <com.google.android.material.button.MaterialButton
                    android:id="@+id/btnGoogleLogin"
                    style="@style/Widget.MaterialComponents.Button.OutlinedButton"
                    android:layout_width="match_parent"
                    android:layout_height="56dp"
                    android:text="CONTINUE WITH GOOGLE"
                    android:textSize="13sp"
                    android:fontFamily="sans-serif-medium"
                    android:letterSpacing="0.05"
                    app:cornerRadius="12dp"
                    app:strokeColor="@color/border_color"
                    app:strokeWidth="1dp"
                    android:textColor="@color/text_primary"
                    app:icon="@drawable/ic_google"
                    app:iconTint="@null"
                    app:iconGravity="textStart"
                    app:iconPadding="12dp"
                    android:stateListAnimator="@null"
                    android:layout_marginBottom="12dp" />

                <com.google.android.material.button.MaterialButton
                    android:id="@+id/btnPhoneLogin"
                    style="@style/Widget.MaterialComponents.Button.OutlinedButton"
                    android:layout_width="match_parent"
                    android:layout_height="56dp"
                    android:text="CONTINUE WITH PHONE"
                    android:textSize="13sp"
                    android:fontFamily="sans-serif-medium"
                    android:letterSpacing="0.05"
                    app:cornerRadius="12dp"
                    app:strokeColor="@color/border_color"
                    app:strokeWidth="1dp"
                    android:textColor="@color/text_primary"
                    app:icon="@drawable/ic_phone"
                    app:iconTint="@color/primary_cyan"
                    app:iconGravity="textStart"
                    app:iconPadding="12dp"
                    android:stateListAnimator="@null"
                    android:layout_marginBottom="32dp" />

            </LinearLayout>

            <View
                android:layout_width="0dp"
                android:layout_height="0dp"
                android:layout_weight="1" />

            <LinearLayout
                android:layout_width="wrap_content"
                android:layout_height="wrap_content"
                android:orientation="horizontal"
                android:gravity="center"
                android:layout_marginBottom="24dp">
                <TextView
                    android:layout_width="wrap_content"
                    android:layout_height="wrap_content"
                    android:text="Don't have an account? "
                    android:fontFamily="sans-serif"
                    android:textSize="14sp"
                    android:textColor="@color/text_secondary" />
                <TextView
                    android:id="@+id/tvRegister"
                    android:layout_width="wrap_content"
                    android:layout_height="wrap_content"
                    android:text="Create Account"
                    android:textSize="14sp"
                    android:fontFamily="sans-serif-medium"
                    android:textColor="@color/primary_cyan"
                    android:padding="8dp"
                    android:clickable="true"
                    android:focusable="true"
                    android:background="?android:attr/selectableItemBackground" />
            </LinearLayout>

            <LinearLayout
                android:layout_width="wrap_content"
                android:layout_height="wrap_content"
                android:orientation="horizontal"
                android:gravity="center_vertical"
                android:layout_marginBottom="16dp">
                <ImageView
                    android:layout_width="16dp"
                    android:layout_height="16dp"
                    android:src="@drawable/ic_shield_check"
                    app:tint="@color/success_green"
                    android:contentDescription="Secure Icon" />
                <TextView
                    android:layout_width="wrap_content"
                    android:layout_height="wrap_content"
                    android:layout_marginStart="6dp"
                    android:text="SentinelX Secure Environment"
                    android:textSize="12sp"
                    android:fontFamily="sans-serif-medium"
                    android:letterSpacing="0.05"
                    android:textColor="@color/success_green" />
            </LinearLayout>

        </LinearLayout>
    </ScrollView>
</androidx.constraintlayout.widget.ConstraintLayout>
''',
    r'D:\SentinelX360\android-app\app\src\main\res\layout\activity_register.xml': '''<?xml version="1.0" encoding="utf-8"?>
<androidx.constraintlayout.widget.ConstraintLayout
    xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:app="http://schemas.android.com/apk/res-auto"
    xmlns:tools="http://schemas.android.com/tools"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:background="@color/bg_deep_navy"
    tools:context=".presentation.ui.auth.RegisterActivity">

    <ScrollView
        android:layout_width="match_parent"
        android:layout_height="match_parent"
        android:fillViewport="true"
        android:scrollbars="none">

        <LinearLayout
            android:layout_width="match_parent"
            android:layout_height="wrap_content"
            android:orientation="vertical"
            android:padding="24dp"
            android:gravity="center_horizontal">

            <View
                android:layout_width="match_parent"
                android:layout_height="16dp" />

            <TextView
                android:layout_width="wrap_content"
                android:layout_height="wrap_content"
                android:text="SentinelX 360"
                android:textSize="32sp"
                android:fontFamily="sans-serif-black"
                android:letterSpacing="0.03"
                android:textColor="@color/text_primary"
                android:layout_marginBottom="4dp" />

            <TextView
                android:layout_width="wrap_content"
                android:layout_height="wrap_content"
                android:text="SECURE DIGITAL PAYMENTS"
                android:textSize="11sp"
                android:fontFamily="sans-serif-medium"
                android:letterSpacing="0.15"
                android:textColor="@color/primary_cyan"
                android:layout_marginBottom="40dp" />

            <LinearLayout
                android:layout_width="match_parent"
                android:layout_height="wrap_content"
                android:orientation="vertical"
                android:gravity="start">

                <TextView
                    android:layout_width="wrap_content"
                    android:layout_height="wrap_content"
                    android:text="Create Account"
                    android:textSize="24sp"
                    android:fontFamily="sans-serif-medium"
                    android:letterSpacing="0.01"
                    android:textColor="@color/text_primary"
                    android:layout_marginBottom="6dp" />

                <TextView
                    android:layout_width="wrap_content"
                    android:layout_height="wrap_content"
                    android:text="Join the secure ecosystem"
                    android:textSize="14sp"
                    android:fontFamily="sans-serif"
                    android:textColor="@color/text_hint"
                    android:layout_marginBottom="24dp" />

                <com.google.android.material.textfield.TextInputLayout
                    android:id="@+id/tilFullName"
                    style="@style/Widget.MaterialComponents.TextInputLayout.OutlinedBox"
                    android:layout_width="match_parent"
                    android:layout_height="wrap_content"
                    android:layout_marginBottom="16dp"
                    app:boxBackgroundColor="@color/bg_surface"
                    app:boxStrokeColor="@color/border_focus"
                    app:boxCornerRadiusBottomEnd="12dp"
                    app:boxCornerRadiusBottomStart="12dp"
                    app:boxCornerRadiusTopEnd="12dp"
                    app:boxCornerRadiusTopStart="12dp"
                    app:hintTextColor="@color/primary_cyan"
                    android:textColorHint="@color/text_hint">

                    <com.google.android.material.textfield.TextInputEditText
                        android:id="@+id/etFullName"
                        android:layout_width="match_parent"
                        android:layout_height="wrap_content"
                        android:hint="Full Name"
                        android:fontFamily="sans-serif"
                        android:inputType="textPersonName"
                        android:textColor="@color/text_primary"
                        android:padding="16dp" />
                </com.google.android.material.textfield.TextInputLayout>

                <com.google.android.material.textfield.TextInputLayout
                    android:id="@+id/tilEmail"
                    style="@style/Widget.MaterialComponents.TextInputLayout.OutlinedBox"
                    android:layout_width="match_parent"
                    android:layout_height="wrap_content"
                    android:layout_marginBottom="16dp"
                    app:boxBackgroundColor="@color/bg_surface"
                    app:boxStrokeColor="@color/border_focus"
                    app:boxCornerRadiusBottomEnd="12dp"
                    app:boxCornerRadiusBottomStart="12dp"
                    app:boxCornerRadiusTopEnd="12dp"
                    app:boxCornerRadiusTopStart="12dp"
                    app:hintTextColor="@color/primary_cyan"
                    android:textColorHint="@color/text_hint">

                    <com.google.android.material.textfield.TextInputEditText
                        android:id="@+id/etEmail"
                        android:layout_width="match_parent"
                        android:layout_height="wrap_content"
                        android:hint="Email Address"
                        android:fontFamily="sans-serif"
                        android:inputType="textEmailAddress"
                        android:textColor="@color/text_primary"
                        android:padding="16dp" />
                </com.google.android.material.textfield.TextInputLayout>

                <com.google.android.material.textfield.TextInputLayout
                    android:id="@+id/tilPassword"
                    style="@style/Widget.MaterialComponents.TextInputLayout.OutlinedBox"
                    android:layout_width="match_parent"
                    android:layout_height="wrap_content"
                    android:layout_marginBottom="32dp"
                    app:passwordToggleEnabled="true"
                    app:passwordToggleTint="@color/text_secondary"
                    app:boxBackgroundColor="@color/bg_surface"
                    app:boxStrokeColor="@color/border_focus"
                    app:boxCornerRadiusBottomEnd="12dp"
                    app:boxCornerRadiusBottomStart="12dp"
                    app:boxCornerRadiusTopEnd="12dp"
                    app:boxCornerRadiusTopStart="12dp"
                    app:hintTextColor="@color/primary_cyan"
                    android:textColorHint="@color/text_hint">

                    <com.google.android.material.textfield.TextInputEditText
                        android:id="@+id/etPassword"
                        android:layout_width="match_parent"
                        android:layout_height="wrap_content"
                        android:hint="Password"
                        android:fontFamily="sans-serif"
                        android:inputType="textPassword"
                        android:textColor="@color/text_primary"
                        android:padding="16dp" />
                </com.google.android.material.textfield.TextInputLayout>

                <FrameLayout
                    android:layout_width="match_parent"
                    android:layout_height="56dp"
                    android:layout_marginBottom="24dp">
                    
                    <com.google.android.material.button.MaterialButton
                        android:id="@+id/btnRegister"
                        android:layout_width="match_parent"
                        android:layout_height="match_parent"
                        android:text="CREATE ACCOUNT"
                        android:textSize="15sp"
                        android:fontFamily="sans-serif-medium"
                        android:letterSpacing="0.08"
                        app:cornerRadius="12dp"
                        app:backgroundTint="@color/primary_cyan"
                        android:textColor="@color/white"
                        android:stateListAnimator="@null" />

                    <ProgressBar
                        android:id="@+id/progressBar"
                        android:layout_width="24dp"
                        android:layout_height="24dp"
                        android:layout_gravity="center"
                        android:visibility="gone"
                        android:indeterminateTint="@color/white" />
                </FrameLayout>

                <LinearLayout
                    android:layout_width="match_parent"
                    android:layout_height="wrap_content"
                    android:orientation="horizontal"
                    android:gravity="center"
                    android:layout_marginBottom="24dp">
                    
                    <View
                        android:layout_width="0dp"
                        android:layout_height="1dp"
                        android:layout_weight="1"
                        android:background="@color/border_color" />
                        
                    <TextView
                        android:layout_width="wrap_content"
                        android:layout_height="wrap_content"
                        android:text="OR"
                        android:fontFamily="sans-serif-medium"
                        android:textColor="@color/text_secondary"
                        android:textSize="12sp"
                        android:layout_marginHorizontal="16dp" />
                        
                    <View
                        android:layout_width="0dp"
                        android:layout_height="1dp"
                        android:layout_weight="1"
                        android:background="@color/border_color" />
                </LinearLayout>

                <com.google.android.material.button.MaterialButton
                    android:id="@+id/btnGoogleRegister"
                    style="@style/Widget.MaterialComponents.Button.OutlinedButton"
                    android:layout_width="match_parent"
                    android:layout_height="56dp"
                    android:text="SIGN UP WITH GOOGLE"
                    android:textSize="13sp"
                    android:fontFamily="sans-serif-medium"
                    android:letterSpacing="0.05"
                    app:cornerRadius="12dp"
                    app:strokeColor="@color/border_color"
                    app:strokeWidth="1dp"
                    android:textColor="@color/text_primary"
                    app:icon="@drawable/ic_google"
                    app:iconTint="@null"
                    app:iconGravity="textStart"
                    app:iconPadding="12dp"
                    android:stateListAnimator="@null"
                    android:layout_marginBottom="12dp" />

                <com.google.android.material.button.MaterialButton
                    android:id="@+id/btnPhoneRegister"
                    style="@style/Widget.MaterialComponents.Button.OutlinedButton"
                    android:layout_width="match_parent"
                    android:layout_height="56dp"
                    android:text="SIGN UP WITH PHONE"
                    android:textSize="13sp"
                    android:fontFamily="sans-serif-medium"
                    android:letterSpacing="0.05"
                    app:cornerRadius="12dp"
                    app:strokeColor="@color/border_color"
                    app:strokeWidth="1dp"
                    android:textColor="@color/text_primary"
                    app:icon="@drawable/ic_phone"
                    app:iconTint="@color/primary_cyan"
                    app:iconGravity="textStart"
                    app:iconPadding="12dp"
                    android:stateListAnimator="@null"
                    android:layout_marginBottom="32dp" />

            </LinearLayout>

            <View
                android:layout_width="0dp"
                android:layout_height="0dp"
                android:layout_weight="1" />

            <LinearLayout
                android:layout_width="wrap_content"
                android:layout_height="wrap_content"
                android:orientation="horizontal"
                android:gravity="center"
                android:layout_marginBottom="24dp">
                <TextView
                    android:layout_width="wrap_content"
                    android:layout_height="wrap_content"
                    android:text="Already have an account? "
                    android:fontFamily="sans-serif"
                    android:textSize="14sp"
                    android:textColor="@color/text_secondary" />
                <TextView
                    android:id="@+id/tvBackToLogin"
                    android:layout_width="wrap_content"
                    android:layout_height="wrap_content"
                    android:text="Login"
                    android:textSize="14sp"
                    android:fontFamily="sans-serif-medium"
                    android:textColor="@color/primary_cyan"
                    android:padding="8dp"
                    android:clickable="true"
                    android:focusable="true"
                    android:background="?android:attr/selectableItemBackground" />
            </LinearLayout>

            <LinearLayout
                android:layout_width="wrap_content"
                android:layout_height="wrap_content"
                android:orientation="horizontal"
                android:gravity="center_vertical"
                android:layout_marginBottom="16dp">
                <ImageView
                    android:layout_width="16dp"
                    android:layout_height="16dp"
                    android:src="@drawable/ic_shield_check"
                    app:tint="@color/success_green"
                    android:contentDescription="Secure Icon" />
                <TextView
                    android:layout_width="wrap_content"
                    android:layout_height="wrap_content"
                    android:layout_marginStart="6dp"
                    android:text="SentinelX Secure Environment"
                    android:textSize="12sp"
                    android:fontFamily="sans-serif-medium"
                    android:letterSpacing="0.05"
                    android:textColor="@color/success_green" />
            </LinearLayout>

        </LinearLayout>
    </ScrollView>
</androidx.constraintlayout.widget.ConstraintLayout>
''',
    r'D:\SentinelX360\android-app\app\src\main\res\drawable\ic_google.xml': '''<vector xmlns:android="http://schemas.android.com/apk/res/android"
    android:width="24dp"
    android:height="24dp"
    android:viewportWidth="24"
    android:viewportHeight="24">
    <path
        android:fillColor="#4285F4"
        android:pathData="M22.56,12.23c0,-0.8 -0.07,-1.56 -0.2,-2.3H12v4.34h5.92c-0.25,1.4 -1.02,2.59 -2.18,3.37v2.8h3.53C21.34,18.53 22.56,15.65 22.56,12.23z"/>
    <path
        android:fillColor="#34A853"
        android:pathData="M12,23c2.97,0 5.46,-0.98 7.28,-2.66l-3.53,-2.8c-0.98,0.66 -2.24,1.05 -3.75,1.05c-2.88,0 -5.32,-1.95 -6.19,-4.57H2.18v2.9C4.01,20.53 7.7,23 12,23z"/>
    <path
        android:fillColor="#FBBC05"
        android:pathData="M5.81,14.02c-0.22,-0.66 -0.35,-1.36 -0.35,-2.09s0.13,-1.43 0.35,-2.09V6.94H2.18C1.43,8.44 1,10.15 1,11.93s0.43,3.49 1.18,4.99L5.81,14.02z"/>
    <path
        android:fillColor="#EA4335"
        android:pathData="M12,5.38c1.62,0 3.06,0.56 4.21,1.64l3.15,-3.15C17.45,2.09 14.97,1 12,1C7.7,1 4.01,3.47 2.18,6.94l3.63,2.9C6.68,7.33 9.12,5.38 12,5.38z"/>
</vector>''',
    r'D:\SentinelX360\android-app\app\src\main\res\drawable\ic_phone.xml': '''<vector xmlns:android="http://schemas.android.com/apk/res/android"
    android:width="24dp"
    android:height="24dp"
    android:viewportWidth="24"
    android:viewportHeight="24">
    <path
        android:fillColor="#00000000"
        android:strokeColor="#FFFFFF"
        android:strokeWidth="2"
        android:pathData="M6.62,10.79c1.44,2.83 3.76,5.14 6.59,6.59l2.2,-2.2c0.27,-0.27 0.67,-0.36 1.02,-0.24c1.12,0.37 2.33,0.57 3.57,0.57c0.55,0 1,0.45 1,1v3.49c0,0.55 -0.45,1 -1,1c-9.39,0 -17,-7.61 -17,-17c0,-0.55 0.45,-1 1,-1h3.5c0.55,0 1,0.45 1,1c0,1.25 0.2,2.45 0.57,3.57c0.11,0.35 0.03,0.74 -0.25,1.02l-2.2,2.2z"/>
</vector>'''
}

for path, content in files.items():
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content.strip() + '\n')
    print(f"Wrote {path}")

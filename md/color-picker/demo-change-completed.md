## zh-CN

颜色选择完成才会触发回调

## en-US

The callback will be called only when the color selection is completed.
```tsx
import React, { useState } from 'react';
import { App, ColorPicker } from 'antd';
import type { ColorPickerProps } from 'antd';

const Demo = () => {
  const { message } = App.useApp();
  const [value, setValue] = useState<ColorPickerProps['value']>('#1677ff');
  return (
    <App>
      <ColorPicker
        value={value}
        onChangeComplete={(color) => {
          setValue(color);
          message.success(`The selected color is ${color.toHexString()}`);
        }}
      />
    </App>
  );
};

export default Demo;
```

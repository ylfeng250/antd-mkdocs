## zh-CN

调试用组件，请勿直接使用。

## en-US

Debug usage. Do not use in your production.
```tsx
import React from 'react';
import { TimePicker } from 'antd';

const { _InternalPanelDoNotUseOrYouWillBeFired: InternalTimePicker } = TimePicker;

const App: React.FC = () => <InternalTimePicker />;

export default App;
```

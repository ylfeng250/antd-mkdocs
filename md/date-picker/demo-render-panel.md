## zh-CN

调试用组件，请勿直接使用。

## en-US

Debug usage. Do not use in your production.
```tsx
import React from 'react';
import { DatePicker } from 'antd';

const { _InternalPanelDoNotUseOrYouWillBeFired: InternalDatePicker } = DatePicker;

const App: React.FC = () => <InternalDatePicker />;

export default App;
```

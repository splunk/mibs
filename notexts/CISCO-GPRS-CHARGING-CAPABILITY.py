#
# PySNMP MIB module CISCO-GPRS-CHARGING-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-GPRS-CHARGING-CAPABILITY
# Produced by pysmi-1.1.12 at Thu Nov 19 08:32:22 2026
# On host runnervmccnms platform Linux version 7.0.0-1019-azure by user runner
# Using Python version 3.11.18 (main, Oct 26 2026, 02:48:29) [GCC 15.2.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
ModuleCompliance, NotificationGroup, AgentCapabilities = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "AgentCapabilities")
ModuleIdentity, TimeTicks, IpAddress, Bits, ObjectIdentity, NotificationType, Gauge32, Counter64, Unsigned32, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, Integer32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "TimeTicks", "IpAddress", "Bits", "ObjectIdentity", "NotificationType", "Gauge32", "Counter64", "Unsigned32", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "Integer32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoGprschargingCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 297))
ciscoGprschargingCapability.setRevisions(('2004-02-03 22:30', '2003-04-08 17:30',))
if mibBuilder.loadTexts: ciscoGprschargingCapability.setLastUpdated('200402032230Z')
if mibBuilder.loadTexts: ciscoGprschargingCapability.setOrganization('Cisco Systems, Inc.')
cGprschargingCapabilityV12R2M8YD = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 297, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cGprschargingCapabilityV12R2M8YD = cGprschargingCapabilityV12R2M8YD.setProductRelease('Cisco IOS 12.2(4)MX & 12.2(8)YD')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cGprschargingCapabilityV12R2M8YD = cGprschargingCapabilityV12R2M8YD.setStatus('current')
cGprschargingCapabilityV12R2M8YY1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 297, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cGprschargingCapabilityV12R2M8YY1 = cGprschargingCapabilityV12R2M8YY1.setProductRelease('Cisco IOS 12.2(8)YY1')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cGprschargingCapabilityV12R2M8YY1 = cGprschargingCapabilityV12R2M8YY1.setStatus('current')
cGprschargingCapabilityV12R2M8YW = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 297, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cGprschargingCapabilityV12R2M8YW = cGprschargingCapabilityV12R2M8YW.setProductRelease('Cisco IOS 12.2(8)YW')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cGprschargingCapabilityV12R2M8YW = cGprschargingCapabilityV12R2M8YW.setStatus('current')
cGprschargingCapabilityV12R3M2XB1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 297, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cGprschargingCapabilityV12R3M2XB1 = cGprschargingCapabilityV12R3M2XB1.setProductRelease('Cisco IOS 12.3(2)XB1')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cGprschargingCapabilityV12R3M2XB1 = cGprschargingCapabilityV12R3M2XB1.setStatus('current')
mibBuilder.exportSymbols("CISCO-GPRS-CHARGING-CAPABILITY", cGprschargingCapabilityV12R3M2XB1=cGprschargingCapabilityV12R3M2XB1, ciscoGprschargingCapability=ciscoGprschargingCapability, cGprschargingCapabilityV12R2M8YD=cGprschargingCapabilityV12R2M8YD, cGprschargingCapabilityV12R2M8YY1=cGprschargingCapabilityV12R2M8YY1, PYSNMP_MODULE_ID=ciscoGprschargingCapability, cGprschargingCapabilityV12R2M8YW=cGprschargingCapabilityV12R2M8YW)

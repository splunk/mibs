#
# PySNMP MIB module CISCO-GPRS-CHARGING-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-GPRS-CHARGING-CAPABILITY
# Produced by pysmi-1.1.12 at Thu Nov 19 14:34:43 2026
# On host runnervmccnms platform Linux version 7.0.0-1019-azure by user runner
# Using Python version 3.11.18 (main, Oct 26 2026, 02:48:29) [GCC 15.2.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
ModuleCompliance, AgentCapabilities, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "AgentCapabilities", "NotificationGroup")
NotificationType, TimeTicks, IpAddress, ObjectIdentity, Unsigned32, Gauge32, ModuleIdentity, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, Bits, iso, Counter64, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "TimeTicks", "IpAddress", "ObjectIdentity", "Unsigned32", "Gauge32", "ModuleIdentity", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "Bits", "iso", "Counter64", "Counter32")
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
mibBuilder.exportSymbols("CISCO-GPRS-CHARGING-CAPABILITY", cGprschargingCapabilityV12R2M8YY1=cGprschargingCapabilityV12R2M8YY1, cGprschargingCapabilityV12R2M8YD=cGprschargingCapabilityV12R2M8YD, cGprschargingCapabilityV12R2M8YW=cGprschargingCapabilityV12R2M8YW, cGprschargingCapabilityV12R3M2XB1=cGprschargingCapabilityV12R3M2XB1, ciscoGprschargingCapability=ciscoGprschargingCapability, PYSNMP_MODULE_ID=ciscoGprschargingCapability)

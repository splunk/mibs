#
# PySNMP MIB module CISCO-DSP-MGMT-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-DSP-MGMT-CAPABILITY
# Produced by pysmi-1.1.12 at Thu Nov 26 06:07:01 2026
# On host runnervm0hi8g platform Linux version 7.0.0-1020-azure by user runner
# Using Python version 3.13.18 (main, Oct 26 2026, 14:19:33) [GCC 15.2.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Counter64, TimeTicks, NotificationType, iso, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, IpAddress, Bits, Gauge32, MibIdentifier, Counter32, Unsigned32, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "TimeTicks", "NotificationType", "iso", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "IpAddress", "Bits", "Gauge32", "MibIdentifier", "Counter32", "Unsigned32", "ObjectIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoDspMgmtCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 121))
ciscoDspMgmtCapability.setRevisions(('2011-04-18 00:00', '2006-08-09 00:00', '2005-10-16 00:00', '2005-06-29 00:00', '2005-04-21 00:00', '2004-08-07 00:00', '2003-09-18 00:00',))
if mibBuilder.loadTexts: ciscoDspMgmtCapability.setLastUpdated('201104180000Z')
if mibBuilder.loadTexts: ciscoDspMgmtCapability.setOrganization('Cisco Systems, Inc.')
ciscoDspMgmtCapabilityV5R00 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 121, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoDspMgmtCapabilityV5R00 = ciscoDspMgmtCapabilityV5R00.setProductRelease('MGX8850 Release 5.0.0')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoDspMgmtCapabilityV5R00 = ciscoDspMgmtCapabilityV5R00.setStatus('current')
ciscoDspMgmtCapabilityV5R015 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 121, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoDspMgmtCapabilityV5R015 = ciscoDspMgmtCapabilityV5R015.setProductRelease('MGX8850 Release 5.0.15')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoDspMgmtCapabilityV5R015 = ciscoDspMgmtCapabilityV5R015.setStatus('current')
ciscoDspMgmtCapabilityV5R100 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 121, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoDspMgmtCapabilityV5R100 = ciscoDspMgmtCapabilityV5R100.setProductRelease('MGX8880 Release 5.1.00')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoDspMgmtCapabilityV5R100 = ciscoDspMgmtCapabilityV5R100.setStatus('current')
ciscoDspMgmtCapabilityV12R03 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 121, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoDspMgmtCapabilityV12R03 = ciscoDspMgmtCapabilityV12R03.setProductRelease('Cisco IOS 12.3')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoDspMgmtCapabilityV12R03 = ciscoDspMgmtCapabilityV12R03.setStatus('current')
ciscoDspMgmtCapabilityV5R300 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 121, 5))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoDspMgmtCapabilityV5R300 = ciscoDspMgmtCapabilityV5R300.setProductRelease('MGX8880 Release 5.3.00')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoDspMgmtCapabilityV5R300 = ciscoDspMgmtCapabilityV5R300.setStatus('current')
ciscoDspMgmtCapabilityV5R400 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 121, 6))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoDspMgmtCapabilityV5R400 = ciscoDspMgmtCapabilityV5R400.setProductRelease('MGX8880 Release 5.4.00')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoDspMgmtCapabilityV5R400 = ciscoDspMgmtCapabilityV5R400.setStatus('current')
ciscoDspMgmtCapabilityV15R02 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 121, 7))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoDspMgmtCapabilityV15R02 = ciscoDspMgmtCapabilityV15R02.setProductRelease('OS=IOS\n                     OSVERSION=15.2(1)T\n                     PLATFORM=c29xx,c3925,c3945,c3925E,c3945E\n                     INTERFACE=None')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoDspMgmtCapabilityV15R02 = ciscoDspMgmtCapabilityV15R02.setStatus('current')
mibBuilder.exportSymbols("CISCO-DSP-MGMT-CAPABILITY", ciscoDspMgmtCapabilityV5R300=ciscoDspMgmtCapabilityV5R300, ciscoDspMgmtCapabilityV5R100=ciscoDspMgmtCapabilityV5R100, ciscoDspMgmtCapabilityV12R03=ciscoDspMgmtCapabilityV12R03, ciscoDspMgmtCapability=ciscoDspMgmtCapability, ciscoDspMgmtCapabilityV15R02=ciscoDspMgmtCapabilityV15R02, ciscoDspMgmtCapabilityV5R00=ciscoDspMgmtCapabilityV5R00, ciscoDspMgmtCapabilityV5R400=ciscoDspMgmtCapabilityV5R400, PYSNMP_MODULE_ID=ciscoDspMgmtCapability, ciscoDspMgmtCapabilityV5R015=ciscoDspMgmtCapabilityV5R015)

#
# PySNMP MIB module CISCO-GTP-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-GTP-CAPABILITY
# Produced by pysmi-1.1.12 at Thu Nov 26 06:06:57 2026
# On host runnervm0hi8g platform Linux version 7.0.0-1020-azure by user runner
# Using Python version 3.13.18 (main, Oct 26 2026, 14:19:33) [GCC 15.2.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Counter64, TimeTicks, NotificationType, Integer32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, IpAddress, Bits, Gauge32, Unsigned32, MibIdentifier, Counter32, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "TimeTicks", "NotificationType", "Integer32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "IpAddress", "Bits", "Gauge32", "Unsigned32", "MibIdentifier", "Counter32", "ObjectIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoGtpCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 263))
ciscoGtpCapability.setRevisions(('2003-04-02 09:00', '2002-03-21 16:00',))
if mibBuilder.loadTexts: ciscoGtpCapability.setLastUpdated('200304020900Z')
if mibBuilder.loadTexts: ciscoGtpCapability.setOrganization('Cisco Systems, Inc.')
cGtpCapabilityV12R02Rev08YD = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 263, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cGtpCapabilityV12R02Rev08YD = cGtpCapabilityV12R02Rev08YD.setProductRelease('Cisco IOS 12.2(8)YD')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cGtpCapabilityV12R02Rev08YD = cGtpCapabilityV12R02Rev08YD.setStatus('current')
cGtpCapabilityV12R02Rev08YY = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 263, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cGtpCapabilityV12R02Rev08YY = cGtpCapabilityV12R02Rev08YY.setProductRelease('Cisco IOS 12.2(8)YY')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cGtpCapabilityV12R02Rev08YY = cGtpCapabilityV12R02Rev08YY.setStatus('current')
cGtpCapabilityV12R02Rev08YW = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 263, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cGtpCapabilityV12R02Rev08YW = cGtpCapabilityV12R02Rev08YW.setProductRelease('Cisco IOS 12.2(8)YW')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cGtpCapabilityV12R02Rev08YW = cGtpCapabilityV12R02Rev08YW.setStatus('current')
mibBuilder.exportSymbols("CISCO-GTP-CAPABILITY", PYSNMP_MODULE_ID=ciscoGtpCapability, ciscoGtpCapability=ciscoGtpCapability, cGtpCapabilityV12R02Rev08YW=cGtpCapabilityV12R02Rev08YW, cGtpCapabilityV12R02Rev08YD=cGtpCapabilityV12R02Rev08YD, cGtpCapabilityV12R02Rev08YY=cGtpCapabilityV12R02Rev08YY)

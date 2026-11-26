#
# PySNMP MIB module CISCO-DIGITAL-MEDIA-SYSTEMS-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-DIGITAL-MEDIA-SYSTEMS-CAPABILITY
# Produced by pysmi-1.1.12 at Thu Nov 26 06:06:59 2026
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
ciscoDigitalMediaSystemsCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 570))
ciscoDigitalMediaSystemsCapability.setRevisions(('2008-06-04 00:00',))
if mibBuilder.loadTexts: ciscoDigitalMediaSystemsCapability.setLastUpdated('200806040000Z')
if mibBuilder.loadTexts: ciscoDigitalMediaSystemsCapability.setOrganization('Cisco Systems, Inc.')
ciscoDigitalMediaSystemsCapabilityV5R00 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 570, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoDigitalMediaSystemsCapabilityV5R00 = ciscoDigitalMediaSystemsCapabilityV5R00.setProductRelease('DMS Release 5.0.0')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoDigitalMediaSystemsCapabilityV5R00 = ciscoDigitalMediaSystemsCapabilityV5R00.setStatus('current')
mibBuilder.exportSymbols("CISCO-DIGITAL-MEDIA-SYSTEMS-CAPABILITY", ciscoDigitalMediaSystemsCapability=ciscoDigitalMediaSystemsCapability, ciscoDigitalMediaSystemsCapabilityV5R00=ciscoDigitalMediaSystemsCapabilityV5R00, PYSNMP_MODULE_ID=ciscoDigitalMediaSystemsCapability)

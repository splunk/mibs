#
# PySNMP MIB module CISCO-INT-SERV-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-INT-SERV-CAPABILITY
# Produced by pysmi-1.1.12 at Thu Nov 26 06:07:46 2026
# On host runnervm0hi8g platform Linux version 7.0.0-1020-azure by user runner
# Using Python version 3.13.18 (main, Oct 26 2026, 14:19:33) [GCC 15.2.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "NotificationGroup", "ModuleCompliance")
Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, ModuleIdentity, MibIdentifier, iso, Counter32, IpAddress, Integer32, NotificationType, ObjectIdentity, Unsigned32, Bits, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "ModuleIdentity", "MibIdentifier", "iso", "Counter32", "IpAddress", "Integer32", "NotificationType", "ObjectIdentity", "Unsigned32", "Bits", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ciscoIntServCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 9999))
if mibBuilder.loadTexts: ciscoIntServCapability.setLastUpdated('200206210000Z')
if mibBuilder.loadTexts: ciscoIntServCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoIntServCapability.setContactInfo('       Cisco Systems\n                        Customer Service\n\n                Postal: 170 W Tasman Drive\n                        San Jose, CA  95134\n                        USA\n\n                        Tel: +1 800 553-NETS\n\n                E-mail: cs-rsvp@cisco.com')
if mibBuilder.loadTexts: ciscoIntServCapability.setDescription('The Agent Capabilities for INT-SERV-MIB.')
ciscoIntServCapabilityVismV3R00 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 9999, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIntServCapabilityVismV3R00 = ciscoIntServCapabilityVismV3R00.setProductRelease('VISM Release 3.00')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIntServCapabilityVismV3R00 = ciscoIntServCapabilityVismV3R00.setStatus('current')
if mibBuilder.loadTexts: ciscoIntServCapabilityVismV3R00.setDescription('INT-SERV-MIB Capabilities.')
mibBuilder.exportSymbols("CISCO-INT-SERV-CAPABILITY", ciscoIntServCapabilityVismV3R00=ciscoIntServCapabilityVismV3R00, ciscoIntServCapability=ciscoIntServCapability, PYSNMP_MODULE_ID=ciscoIntServCapability)

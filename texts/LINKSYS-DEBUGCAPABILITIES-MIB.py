#
# PySNMP MIB module LINKSYS-DEBUGCAPABILITIES-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/linksys/LINKSYS-DEBUGCAPABILITIES-MIB
# Produced by pysmi-1.1.12 at Thu Nov 26 06:12:02 2026
# On host runnervm0hi8g platform Linux version 7.0.0-1020-azure by user runner
# Using Python version 3.13.18 (main, Oct 26 2026, 14:19:33) [GCC 15.2.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint")
rnd, = mibBuilder.importSymbols("LINKSYS-MIB", "rnd")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Integer32, Counter32, Gauge32, Unsigned32, NotificationType, iso, Bits, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, Counter64, MibIdentifier, IpAddress, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "Counter32", "Gauge32", "Unsigned32", "NotificationType", "iso", "Bits", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "Counter64", "MibIdentifier", "IpAddress", "ObjectIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
rlDebugCapabilities = ModuleIdentity((1, 3, 6, 1, 4, 1, 3955, 1000, 201, 206))
rlDebugCapabilities.setRevisions(('2011-01-05 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: rlDebugCapabilities.setRevisionsDescriptions(('Initial revision.',))
if mibBuilder.loadTexts: rlDebugCapabilities.setLastUpdated('201101050000Z')
if mibBuilder.loadTexts: rlDebugCapabilities.setOrganization('\n                              Linksys LLC.')
if mibBuilder.loadTexts: rlDebugCapabilities.setContactInfo('www.linksys.com/business/support')
if mibBuilder.loadTexts: rlDebugCapabilities.setDescription('This private MIB module is used for achieving extended\n                      debugging capablities for the device.\n                      For example: greater management capabilies for technical\n                      support users.')
rlDebugCapabilitiesPassword = MibScalar((1, 3, 6, 1, 4, 1, 3955, 1000, 201, 206, 1), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlDebugCapabilitiesPassword.setStatus('current')
if mibBuilder.loadTexts: rlDebugCapabilitiesPassword.setDescription('A user intereseted to obtain extended debug capabilities should\n            SET this MIB to a well known secret value (it is intended to be\n            used only by authorized users).\n            Most often, this value will be based on the device MAC address.\n            Upon setting the correct value, the SET operation will return\n            noError. Otherwise, wrongValue will return to the caller.\n            GET operation on this MIB will reurn a value of length 0.')
mibBuilder.exportSymbols("LINKSYS-DEBUGCAPABILITIES-MIB", rlDebugCapabilitiesPassword=rlDebugCapabilitiesPassword, rlDebugCapabilities=rlDebugCapabilities, PYSNMP_MODULE_ID=rlDebugCapabilities)

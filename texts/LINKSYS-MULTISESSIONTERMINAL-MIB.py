#
# PySNMP MIB module LINKSYS-MULTISESSIONTERMINAL-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/linksys/LINKSYS-MULTISESSIONTERMINAL-MIB
# Produced by pysmi-1.1.12 at Thu Nov 19 08:37:19 2026
# On host runnervmccnms platform Linux version 7.0.0-1019-azure by user runner
# Using Python version 3.11.18 (main, Oct 26 2026, 02:48:29) [GCC 15.2.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint")
rnd, = mibBuilder.importSymbols("LINKSYS-MIB", "rnd")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Counter64, MibIdentifier, Bits, Counter32, Gauge32, IpAddress, Unsigned32, ModuleIdentity, TimeTicks, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, Integer32, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "MibIdentifier", "Bits", "Counter32", "Gauge32", "IpAddress", "Unsigned32", "ModuleIdentity", "TimeTicks", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "Integer32", "ObjectIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
rlMultiSessionTerminal = ModuleIdentity((1, 3, 6, 1, 4, 1, 3955, 1000, 201, 69))
rlMultiSessionTerminal.setRevisions(('2007-01-02 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: rlMultiSessionTerminal.setRevisionsDescriptions(('Initial revision.',))
if mibBuilder.loadTexts: rlMultiSessionTerminal.setLastUpdated('200701020000Z')
if mibBuilder.loadTexts: rlMultiSessionTerminal.setOrganization('\n                              Linksys LLC.')
if mibBuilder.loadTexts: rlMultiSessionTerminal.setContactInfo('www.linksys.com/business/support')
if mibBuilder.loadTexts: rlMultiSessionTerminal.setDescription('This private MIB module defines Multi Session Terminal private MIBs.')
rlTerminalDebugModePassword = MibScalar((1, 3, 6, 1, 4, 1, 3955, 1000, 201, 69, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 20))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlTerminalDebugModePassword.setStatus('current')
if mibBuilder.loadTexts: rlTerminalDebugModePassword.setDescription('When a user wants to change the terminal mode\n            from debug mode to ASCII he must enter this password first')
mibBuilder.exportSymbols("LINKSYS-MULTISESSIONTERMINAL-MIB", rlMultiSessionTerminal=rlMultiSessionTerminal, PYSNMP_MODULE_ID=rlMultiSessionTerminal, rlTerminalDebugModePassword=rlTerminalDebugModePassword)
